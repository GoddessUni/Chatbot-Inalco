import argparse
import json
from pathlib import Path

from hash_embedder import embed_text


def load_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def save_jsonl(records: list[dict], path: str | Path) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def index_record(chunk: dict, dim: int) -> dict:
    text = chunk.get("embedding_text") or chunk.get("text", "")
    return {
        "chunk_id": chunk.get("chunk_id"),
        "vector": embed_text(text, dim=dim),
        "text": chunk.get("text"),
        "embedding_text": text,
        "metadata": {
            "source_url": chunk.get("source_url"),
            "source_urls": chunk.get("source_urls", [chunk.get("source_url")]),
            "title": chunk.get("title"),
            "section_title": chunk.get("section_title"),
            "theme": chunk.get("theme"),
            "knowledge_type": chunk.get("knowledge_type"),
            "risk_level": chunk.get("risk_level"),
            "quality_status": chunk.get("quality_status"),
            "review_priority": chunk.get("review_priority"),
            "quality_flags": chunk.get("quality_flags", []),
            "source_domain": chunk.get("source_domain"),
            "source_scope": chunk.get("source_scope"),
            "last_seen": chunk.get("last_seen"),
            "prototype_trusted": chunk.get("prototype_trusted", False),
        },
    }


def build_index(input_path: str | Path, output_path: str | Path, dim: int) -> dict:
    chunks = load_jsonl(input_path)
    records = [index_record(chunk, dim) for chunk in chunks]
    save_jsonl(records, output_path)
    return {
        "input": str(input_path),
        "output": str(output_path),
        "records": len(records),
        "embedding_backend": "hashing",
        "dim": dim,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data/kb/prototype_all_trusted.jsonl",
    )
    parser.add_argument(
        "--output",
        default="indexes/prototype_hash/index.jsonl",
    )
    parser.add_argument("--dim", type=int, default=768)
    args = parser.parse_args()
    summary = build_index(args.input, args.output, args.dim)
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
