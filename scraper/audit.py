import argparse
import json
from collections import Counter
from pathlib import Path


def load_jsonl(path: str) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def audit(pages_path: str, chunks_path: str, review_path: str | None = None) -> None:
    pages = load_jsonl(pages_path)
    chunks = load_jsonl(chunks_path)
    reviews = load_jsonl(review_path) if review_path and Path(review_path).exists() else []

    print(f"Pages: {len(pages)}")
    print(f"Chunks: {len(chunks)}")
    print(f"Unique page URLs: {len({page['source_url'] for page in pages})}")
    print(f"Unique chunk IDs: {len({chunk['chunk_id'] for chunk in chunks})}")
    print("Duplicate pages marked:", sum(page.get("is_duplicate", False) for page in pages))
    print(
        "Chunks with multiple sources:",
        sum(len(chunk.get("source_urls", [])) > 1 for chunk in chunks),
    )
    print()

    print(
        "Knowledge types:",
        Counter(page.get("knowledge_type", "missing") for page in pages),
    )
    print("Themes:", Counter(chunk.get("theme", "missing") for chunk in chunks))
    print("Risk levels:", Counter(chunk.get("risk_level", "missing") for chunk in chunks))
    print()

    print("Missing page titles:", sum(not page.get("title") for page in pages))
    print("Missing chunk titles:", sum(not chunk.get("title") for chunk in chunks))
    print(
        "Missing section titles:",
        sum(not chunk.get("section_title") for chunk in chunks),
    )
    print("Short chunks (<200 chars):", sum(len(chunk["text"]) < 200 for chunk in chunks))
    print("Long chunks (>1800 chars):", sum(len(chunk["text"]) > 1800 for chunk in chunks))
    print(
        "JavaScript noise:",
        sum("javascript:void" in chunk["text"].lower() for chunk in chunks),
    )
    print(
        "Unverified high-risk chunks:",
        sum(
            chunk["risk_level"] == "high" and not chunk.get("human_verified")
            for chunk in chunks
        ),
    )
    print(
        "Quality statuses:",
        Counter(chunk.get("quality_status", "missing") for chunk in chunks),
    )
    print(
        "Quality flags:",
        Counter(flag for chunk in chunks for flag in chunk.get("quality_flags", [])),
    )
    if reviews:
        print(
            "Review priorities:",
            Counter(record["review_priority"] for record in reviews),
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", default="data/pages.jsonl")
    parser.add_argument("--chunks", default="data/chunks.jsonl")
    parser.add_argument("--review", default="data/review_queue.jsonl")
    args = parser.parse_args()
    audit(args.pages, args.chunks, args.review)
