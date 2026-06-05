import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque

from config import (
    BASE_URL,
    ALLOWED_DOMAIN,
    EXCLUDED_EXTENSIONS,
    MAX_PAGES,
    REQUEST_TIMEOUT,
    CRAWL_DELAY,
)


def normalize_url(url: str) -> str:
    return url.split("#")[0].rstrip("/")


def is_allowed_url(url: str) -> bool:
    parsed = urlparse(url)

    if parsed.netloc != ALLOWED_DOMAIN:
        return False

    if not parsed.path.startswith("/fr/"):
        return False

    if parsed.path.lower().endswith(EXCLUDED_EXTENSIONS):
        return False

    return True


def crawl_site() -> list[str]:
    visited = set()
    queue = deque([BASE_URL])
    urls = []

    headers = {
        "User-Agent": "InalcoStudentChatbotResearch/0.1"
    }

    while queue and len(visited) < MAX_PAGES:
        url = normalize_url(queue.popleft())

        if url in visited:
            continue

        visited.add(url)

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
        except requests.RequestException:
            continue

        content_type = response.headers.get("content-type", "")
        if "text/html" not in content_type:
            continue

        urls.append(url)

        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.find_all("a", href=True):
            next_url = normalize_url(urljoin(url, a["href"]))

            if is_allowed_url(next_url) and next_url not in visited:
                queue.append(next_url)

        time.sleep(CRAWL_DELAY)

    return urls