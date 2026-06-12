import re

from config import (
    INVALID_CONTENT_PATTERNS,
    MIN_INDEXABLE_CHARS,
    PLACEHOLDER_CONTENT,
    SHORT_CHUNK_CHARS,
    SHORT_CHUNK_PRIORITY_FACTOR,
)

SENSITIVE_FACT_PATTERNS = {
    "contains_email": re.compile(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"),
    "contains_phone": re.compile(r"(?:\+33|0)\s*[1-9](?:[\s.-]*\d{2}){4}"),
    "contains_amount": re.compile(r"\b\d+(?:[.,]\d+)?\s*€"),
    "contains_date": re.compile(
        r"\b(?:\d{1,2}\s+"
        r"(?:janvier|février|mars|avril|mai|juin|juillet|août|"
        r"septembre|octobre|novembre|décembre)"
        r"|20\d{2}(?:[-–/]20\d{2})?)\b",
        re.IGNORECASE,
    ),
}


def _normalized_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def _has_meaningful_content(text: str) -> bool:
    return any(character.isalnum() for character in text)


def assess_page(page: dict) -> tuple[bool, list[str]]:
    text = _normalized_text(page.get("text", ""))
    reasons = []

    if not text:
        reasons.append("empty_text")

    for pattern in INVALID_CONTENT_PATTERNS:
        if pattern in text:
            reasons.append(f"invalid_content:{pattern}")

    return not reasons, reasons


def assess_chunk(chunk: dict) -> tuple[dict, list[str], list[str]]:
    chunk = dict(chunk)
    text = chunk.get("text", "").strip()
    normalized = _normalized_text(text)
    rejection_reasons = []
    quality_flags = []

    if not _has_meaningful_content(text):
        rejection_reasons.append("no_meaningful_content")

    if len(text) < MIN_INDEXABLE_CHARS:
        rejection_reasons.append("too_short_to_index")

    if normalized in PLACEHOLDER_CONTENT:
        rejection_reasons.append("placeholder_content")

    if "en cours de construction" in normalized:
        if len(text) < 300:
            rejection_reasons.append("construction_placeholder")
        else:
            quality_flags.append("construction_notice")

    for pattern in INVALID_CONTENT_PATTERNS:
        if pattern in normalized:
            rejection_reasons.append(f"invalid_content:{pattern}")

    if rejection_reasons:
        return chunk, rejection_reasons, quality_flags

    if len(text) < SHORT_CHUNK_CHARS:
        quality_flags.append("short_chunk")
        chunk["retrieval_priority"] = round(
            chunk.get("retrieval_priority", 1.0) * SHORT_CHUNK_PRIORITY_FACTOR,
            3,
        )

    if not chunk.get("title"):
        quality_flags.append("missing_title")

    if not chunk.get("section_title"):
        quality_flags.append("missing_section_title")

    if chunk.get("theme") == "Général":
        quality_flags.append("generic_theme")

    if chunk.get("knowledge_type") == "temporal":
        quality_flags.append("temporal_content")

    if chunk.get("has_duplicate_sources"):
        quality_flags.append("multiple_sources")

    for flag, pattern in SENSITIVE_FACT_PATTERNS.items():
        if pattern.search(text):
            quality_flags.append(flag)

    chunk["quality_flags"] = sorted(set(quality_flags))
    chunk["quality_status"] = "review" if quality_flags else "ready"
    return chunk, rejection_reasons, quality_flags


def review_priority(chunk: dict) -> str | None:
    flags = set(chunk.get("quality_flags", []))

    if chunk.get("risk_level") == "high" and flags.intersection(
        {"contains_amount", "contains_date", "contains_phone", "contains_email"}
    ):
        return "P0"

    if chunk.get("risk_level") == "high":
        return "P1"

    if flags.intersection(
        {
            "short_chunk",
            "missing_title",
            "missing_section_title",
            "generic_theme",
            "temporal_content",
            "multiple_sources",
            "construction_notice",
        }
    ):
        return "P2"

    return None


def build_review_record(chunk: dict) -> dict | None:
    priority = review_priority(chunk)
    if priority is None:
        return None

    return {
        "review_priority": priority,
        "chunk_id": chunk.get("chunk_id"),
        "title": chunk.get("title"),
        "section_title": chunk.get("section_title"),
        "theme": chunk.get("theme"),
        "risk_level": chunk.get("risk_level"),
        "quality_flags": chunk.get("quality_flags", []),
        "source_url": chunk.get("source_url"),
        "source_urls": chunk.get("source_urls", [chunk.get("source_url")]),
        "text": chunk.get("text"),
        "verification_status": "pending",
        "verified_by": None,
        "verified_at": None,
        "verification_notes": None,
    }
