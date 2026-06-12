from datetime import date

import trafilatura
from bs4 import BeautifulSoup

from config import MIN_PAGE_CHARS


def _parse_markdown_sections(markdown: str, fallback_title: str) -> list[dict]:
    sections = []
    current_title = fallback_title
    current_lines = []

    def flush() -> None:
        text = "\n".join(current_lines).strip()
        if text:
            sections.append({"section_title": current_title, "text": text})

    for line in markdown.splitlines():
        stripped = line.strip()

        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            if heading:
                flush()
                current_lines = []
                current_title = heading
                continue

        current_lines.append(line)

    flush()
    return sections


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

    markdown = trafilatura.extract(
        downloaded,
        output_format="markdown",
        include_links=True,
        include_tables=True,
        include_comments=False,
        favor_precision=True,
    )
    sections = _parse_markdown_sections(markdown or text, title)

    return {
        "source_url": url,
        "title": title,
        "html_title": html_title,
        "language": "fr",
        "content_type": "web_page",
        "last_seen": str(date.today()),
        "text": text,
        "sections": sections,
    }
