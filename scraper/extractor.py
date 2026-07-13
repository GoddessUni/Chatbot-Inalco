from datetime import date
import re

import trafilatura
from bs4 import BeautifulSoup

from config import MIN_PAGE_CHARS


NOISE_SELECTORS = (
    "script",
    "style",
    "noscript",
    "svg",
    "form",
    "header",
    "footer",
    "nav",
    ".breadcrumb",
    ".breadcrumbs",
    ".search",
    ".menu",
    ".navbar",
    ".pagination",
    ".social",
)

MAIN_SELECTORS = (
    "main",
    "article",
    "[role='main']",
    ".main-content",
    ".content",
    ".page-content",
    ".field--name-body",
    ".node__content",
)

SECTION_HEADING_TAGS = ("h1", "h2", "h3", "h4")


def _normalize_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


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


def _prepare_soup(downloaded: str) -> BeautifulSoup:
    soup = BeautifulSoup(downloaded, "html.parser")
    for selector in NOISE_SELECTORS:
        for element in soup.select(selector):
            element.decompose()
    return soup


def _main_content_node(soup: BeautifulSoup):
    candidates = []
    for selector in MAIN_SELECTORS:
        candidates.extend(soup.select(selector))

    if not candidates:
        return soup.body or soup

    return max(
        candidates,
        key=lambda element: len(element.get_text(" ", strip=True)),
    )


def _element_text(element) -> str:
    lines = []
    for descendant in element.descendants:
        name = getattr(descendant, "name", None)
        if name in SECTION_HEADING_TAGS:
            text = descendant.get_text(" ", strip=True)
            if text:
                level = 1 if name == "h1" else 2 if name == "h2" else 3
                lines.append(f"{'#' * level} {text}")
        elif name == "li":
            text = descendant.get_text(" ", strip=True)
            if text:
                lines.append(f"- {text}")
        elif name in {"p", "div", "address", "td", "th", "caption"}:
            text = descendant.get_text(" ", strip=True)
            if text:
                lines.append(text)

    if not lines:
        return element.get_text("\n", strip=True)

    deduped = []
    previous = None
    for line in lines:
        line = _normalize_text(line)
        if line and line != previous:
            deduped.append(line)
            previous = line

    return _normalize_text("\n".join(deduped))


def _parse_html_sections(downloaded: str, fallback_title: str) -> tuple[str, list[dict]]:
    soup = _prepare_soup(downloaded)
    main = _main_content_node(soup)

    sections = []
    current_title = fallback_title
    current_lines = []

    def flush() -> None:
        text = _normalize_text("\n".join(current_lines))
        if text:
            sections.append({"section_title": current_title, "text": text})

    for element in main.find_all(
        [*SECTION_HEADING_TAGS, "p", "ul", "ol", "table", "address", "details"],
        recursive=True,
    ):
        if any(parent.name in SECTION_HEADING_TAGS for parent in element.parents):
            continue

        if element.name in SECTION_HEADING_TAGS:
            heading = element.get_text(" ", strip=True)
            if heading:
                flush()
                current_lines = []
                current_title = heading
            continue

        if element.find_parent(["p", "ul", "ol", "table", "address", "details"]):
            continue

        text = element.get_text("\n", strip=True)
        if text:
            current_lines.append(text)

    flush()

    if not sections:
        full_text = _element_text(main)
        sections = [{"section_title": fallback_title, "text": full_text}] if full_text else []

    full_text = _normalize_text("\n\n".join(section["text"] for section in sections))
    return full_text, sections


def _merge_sections(primary: list[dict], secondary: list[dict]) -> list[dict]:
    merged = []
    seen = set()

    for section in [*primary, *secondary]:
        title = _normalize_text(section.get("section_title", ""))
        text = _normalize_text(section.get("text", ""))
        if not text:
            continue

        key = (title.lower(), text[:250].lower())
        if key in seen:
            continue

        merged.append({"section_title": title, "text": text})
        seen.add(key)

    return merged


def _choose_text(trafilatura_text: str | None, html_text: str) -> str:
    trafilatura_text = _normalize_text(trafilatura_text or "")
    html_text = _normalize_text(html_text)

    if not trafilatura_text:
        return html_text

    # If the HTML extraction is substantially richer, it likely contains
    # structured cards/accordions that Trafilatura skipped.
    if len(html_text) > len(trafilatura_text) * 1.25:
        return html_text

    return trafilatura_text


def extract_page(url: str) -> dict | None:
    downloaded = trafilatura.fetch_url(url)

    if not downloaded:
        return None

    trafilatura_text = trafilatura.extract(
        downloaded,
        include_links=True,
        include_tables=True,
        include_comments=False,
        favor_precision=True,
    )

    soup = BeautifulSoup(downloaded, "html.parser")
    html_title = soup.title.get_text(" ", strip=True) if soup.title else ""
    h1 = soup.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else html_title
    html_text, html_sections = _parse_html_sections(downloaded, title)
    text = _choose_text(trafilatura_text, html_text)

    if not text or len(text.strip()) < MIN_PAGE_CHARS:
        return None

    markdown = trafilatura.extract(
        downloaded,
        output_format="markdown",
        include_links=True,
        include_tables=True,
        include_comments=False,
        favor_precision=True,
    )
    markdown_sections = _parse_markdown_sections(markdown or trafilatura_text or text, title)
    sections = _merge_sections(html_sections, markdown_sections)

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
