import hashlib


def make_chunk_id(url: str, index: int) -> str:
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{digest}-{index}"


def split_text(text: str, max_chars: int = 1500) -> list[str]:
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]

    chunks = []
    current = ""

    for para in paragraphs:
        if len(current) + len(para) <= max_chars:
            current = f"{current}\n{para}".strip()
        else:
            if current:
                chunks.append(current)
            current = para

    if current:
        chunks.append(current)

    return chunks


def build_chunks(page: dict) -> list[dict]:
    chunks = []

    for i, text in enumerate(split_text(page["text"])):
        chunks.append({
            "chunk_id": make_chunk_id(page["source_url"], i),
            "source_url": page["source_url"],
            "title": page["title"],
            "language": page["language"],
            "content_type": page["content_type"],
            "last_seen": page["last_seen"],
            "text": text
        })

    return chunks