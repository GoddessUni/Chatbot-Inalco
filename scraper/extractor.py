from datetime import date

import trafilatura
from bs4 import BeautifulSoup

from config import MIN_PAGE_CHARS


def extract_page(url: str) -> dict | None:
    downloaded = trafilatura.fetch_url(url)

    if not downloaded:
        return None

    text = trafilatura.extract(
        downloaded,
        include_links=True,
        include_tables=True,
        include_comments=False,
        favor_precision=True,
    )

    if not text or len(text.strip()) < MIN_PAGE_CHARS:
        return None

    soup = BeautifulSoup(downloaded, "html.parser")
    html_title = soup.title.get_text(" ", strip=True) if soup.title else ""
    h1 = soup.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else html_title

    return {
        "source_url": url,
        "title": title,
        "html_title": html_title,
        "language": "fr",
        "content_type": "web_page",
        "last_seen": str(date.today()),
        "text": text,
    }
