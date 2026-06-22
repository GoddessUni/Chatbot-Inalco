import time
from collections import deque
from urllib.parse import urljoin, urlparse, urlunparse

import requests
from bs4 import BeautifulSoup

from config import (
    CRAWL_DELAY,
    EXCLUDED_EXTENSIONS,
    MAX_PAGES,
    REQUEST_TIMEOUT,
    SEED_URLS,
    SOURCE_PROFILES,
    USER_AGENT,
)


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    normalized = parsed._replace(fragment="", query="")
    result = urlunparse(normalized)

    if result.endswith("/") and result != f"{parsed.scheme}://{parsed.netloc}/":
        result = result.rstrip("/")

    return result


def is_allowed_url(url: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path.lower()
    profile = SOURCE_PROFILES.get(parsed.netloc)

    if parsed.scheme not in {"http", "https"}:
        return False

    if not profile:
        return False

    allowed_prefixes = profile.get("allowed_path_prefixes", ())
    if allowed_prefixes and not any(parsed.path.startswith(prefix) for prefix in allowed_prefixes):
        return False

    if path.endswith(EXCLUDED_EXTENSIONS):
        return False

    if any(excluded in parsed.path for excluded in profile.get("excluded_paths", ())):
        return False

    return True


def crawl_site() -> tuple[list[str], list[dict]]:
    visited = set()
    queued = {normalize_url(url) for url in SEED_URLS}
    queue = deque(sorted(queued))
    urls = []
    failures = []

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    while queue and len(visited) < MAX_PAGES:
        url = normalize_url(queue.popleft())

        if url in visited:
            continue

        visited.add(url)

        try:
            response = session.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.RequestException as exc:
            failures.append({"url": url, "stage": "crawl", "error": str(exc)})
            continue

        content_type = response.headers.get("content-type", "").lower()
        if "text/html" not in content_type:
            continue

        urls.append(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            next_url = normalize_url(urljoin(url, link["href"]))

            if (
                is_allowed_url(next_url)
                and next_url not in visited
                and next_url not in queued
            ):
                queue.append(next_url)
                queued.add(next_url)

        time.sleep(CRAWL_DELAY)

    return sorted(set(urls)), failures
