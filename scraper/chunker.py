import hashlib
import re

from config import CHUNK_MAX_CHARS, CHUNK_MIN_CHARS


def make_chunk_id(url: str, index: int) -> str:
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{digest}-{index}"


def _split_long_paragraph(paragraph: str, max_chars: int) -> list[str]:
    sentences = [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", paragraph)
        if sentence.strip()
    ]

    if len(sentences) <= 1:
        return [
            paragraph[start : start + max_chars].strip()
            for start in range(0, len(paragraph), max_chars)
        ]

    pieces = []
    current = ""
    for sentence in sentences:
        candidate = f"{current} {sentence}".strip() if current else sentence

        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                pieces.append(current)
            if len(sentence) > max_chars:
                pieces.extend(
                    sentence[start : start + max_chars].strip()
                    for start in range(0, len(sentence), max_chars)
                )
                current = ""
            else:
                current = sentence

    if current:
        pieces.append(current)

    return pieces


def _merge_short_chunks(chunks: list[str], min_chars: int, max_chars: int) -> list[str]:
    if not chunks:
        return []

    merged = []
    for chunk in chunks:
        candidate = f"{merged[-1]}\n{chunk}".strip() if merged else chunk
        if merged and len(chunk) < min_chars and len(candidate) <= max_chars:
            merged[-1] = candidate
        else:
            merged.append(chunk)
    return merged


def split_text(
    text: str,
    max_chars: int = CHUNK_MAX_CHARS,
    min_chars: int = CHUNK_MIN_CHARS,
) -> list[str]:
    paragraphs = [paragraph.strip() for paragraph in text.split("\n") if paragraph.strip()]
    chunks = []
    current = ""

    for paragraph in paragraphs:
        candidate = f"{current}\n{paragraph}".strip() if current else paragraph

        if len(candidate) <= max_chars:
            current = candidate
            continue

        if current:
            chunks.append(current)

        if len(paragraph) > max_chars:
            chunks.extend(_split_long_paragraph(paragraph, max_chars))
            current = ""
        else:
            current = paragraph

    if current:
        chunks.append(current)

    return _merge_short_chunks(chunks, min_chars, max_chars)


def build_chunks(page: dict) -> list[dict]:
    chunks = []
    sections = page.get("sections") or [
        {"section_title": page.get("title", ""), "text": page["text"]}
    ]
    index = 0

    for section in sections:
        section_title = section.get("section_title") or page.get("title", "")

        for text in split_text(section["text"]):
            chunks.append(
                {
                    "chunk_id": make_chunk_id(page["source_url"], index),
                    "source_url": page["source_url"],
                    "title": page["title"],
                    "section_title": section_title,
                    "language": page["language"],
                    "content_type": page["content_type"],
                    "last_seen": page["last_seen"],
                    "knowledge_type": page["knowledge_type"],
                    "retrieval_priority": page["retrieval_priority"],
                    "source_type": page["source_type"],
                    "human_verified": page["human_verified"],
                    "text": text,
                }
            )
            index += 1

    return chunks
