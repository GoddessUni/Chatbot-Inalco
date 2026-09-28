from __future__ import annotations

from datetime import date
import hashlib
from io import BytesIO
import re
from typing import Any

import requests

from config import MAX_PDF_BYTES, PDF_REQUEST_TIMEOUT, USER_AGENT


HEADING_PATTERN = re.compile(
    r"^(?:[IVX]+[.)-]?\s+|(?:AXE|OBJECTIF|INTRODUCTION|CONCLUSION|ANNEXE|"
    r"GLOSSAIRE|SOMMAIRE|PRIORITÉ|DOMAINE|PARTIE)\b)",
    re.IGNORECASE,
)


def _normalize_pdf_text(text: str) -> str:
    text = (text or "").replace("\x00", "").replace("\xa0", " ")
    text = text.replace("\u00ad", "")
    text = re.sub(r"(?<=\w)-\n(?=\w)", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _looks_like_heading(line: str) -> bool:
    line = " ".join(line.split()).strip(" -–—•")
    if not 4 <= len(line) <= 140:
        return False
    if HEADING_PATTERN.search(line):
        return True
    letters = [character for character in line if character.isalpha()]
    return bool(letters) and len(letters) >= 4 and all(
        character.isupper() for character in letters
    )


def _section_title(text: str, page_number: int) -> str:
    for line in text.splitlines()[:15]:
        candidate = " ".join(line.split()).strip(" -–—•")
        if _looks_like_heading(candidate):
            return f"Page {page_number} - {candidate}"
    return f"Page {page_number}"


def extract_pdf_bytes(data: bytes, source: dict[str, Any]) -> dict:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError(
            "PDF extraction requires pypdf. Install it with: pip install pypdf"
        ) from exc

    if not data.startswith(b"%PDF"):
        raise ValueError("Downloaded content is not a PDF file")

    reader = PdfReader(BytesIO(data), strict=False)
    if reader.is_encrypted:
        try:
            reader.decrypt("")
        except Exception as exc:
            raise ValueError("Encrypted PDF cannot be read") from exc

    sections = []
    page_texts = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            raw_text = page.extract_text(extraction_mode="layout")
        except (TypeError, ValueError):
            raw_text = page.extract_text()
        text = _normalize_pdf_text(raw_text or "")
        if not text:
            continue
        sections.append(
            {
                "section_title": _section_title(text, page_number),
                "text": text,
                "page_start": page_number,
                "page_end": page_number,
            }
        )
        page_texts.append(f"[Page {page_number}]\n{text}")

    if not sections:
        raise ValueError("PDF contains no extractable text; OCR may be required")

    title = source["title"]
    return {
        "source_url": source["source_url"],
        "parent_url": source.get("parent_url"),
        "title": title,
        "document_title": title,
        "html_title": title,
        "language": source.get("language", "fr"),
        "content_type": "pdf",
        "source_type": "official_pdf",
        "knowledge_type": source.get("knowledge_type", "temporal"),
        "validity_period": source.get("validity_period"),
        "last_seen": str(date.today()),
        "file_sha256": hashlib.sha256(data).hexdigest(),
        "file_size_bytes": len(data),
        "pdf_pages_total": len(reader.pages),
        "pdf_pages_extracted": len(sections),
        "text": "\n\n".join(page_texts),
        "sections": sections,
    }


def download_and_extract_pdf(source: dict[str, Any]) -> dict:
    response = requests.get(
        source["source_url"],
        headers={"User-Agent": USER_AGENT},
        timeout=PDF_REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    declared_size = int(response.headers.get("content-length") or 0)
    if declared_size and declared_size > MAX_PDF_BYTES:
        raise ValueError(
            f"PDF exceeds MAX_PDF_BYTES: {declared_size} > {MAX_PDF_BYTES}"
        )
    if len(response.content) > MAX_PDF_BYTES:
        raise ValueError(
            f"PDF exceeds MAX_PDF_BYTES: {len(response.content)} > {MAX_PDF_BYTES}"
        )

    return extract_pdf_bytes(response.content, source)
