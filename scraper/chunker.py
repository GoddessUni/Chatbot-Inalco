import hashlib

from config import CHUNK_MAX_CHARS, CHUNK_MIN_CHARS


def make_chunk_id(url: str, index: int) -> str:
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{digest}-{index}"


def _merge_short_chunks(chunks: list[str], min_chars: int) -> list[str]:
    if not chunks:
        return []

    merged = []
    for chunk in chunks:
        if merged and len(chunk) < min_chars:
            merged[-1] = f"{merged[-1]}\n{chunk}".strip()
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
            start = 0
            while start < len(paragraph):
                chunks.append(paragraph[start : start + max_chars].strip())
                start += max_chars
            current = ""
        else:
            current = paragraph

    if current:
        chunks.append(current)

    return _merge_short_chunks(chunks, min_chars)


def build_chunks(page: dict) -> list[dict]:
    chunks = []

    for index, text in enumerate(split_text(page["text"])):
        chunks.append(
            {
                "chunk_id": make_chunk_id(page["source_url"], index),
                "source_url": page["source_url"],
                "title": page["title"],
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

    return chunks
