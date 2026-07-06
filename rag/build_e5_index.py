import argparse
import json
from pathlib import Path

from e5_embedder import DEFAULT_E5_MODEL, encode_passages


def load_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def save_jsonl(records: list[dict], path: str | Path) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def metadata_for(chunk: dict) -> dict:
    return {
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
        "source_type": chunk.get("source_type"),
        "human_verified": chunk.get("human_verified", False),
        "last_seen": chunk.get("last_seen"),
        "prototype_trusted": chunk.get("prototype_trusted", False),
        "curated_question": chunk.get("curated_question"),
    }


def build_e5_index(
    input_path: str | Path,
    output_path: str | Path,
    model_name: str,
    batch_size: int,
) -> dict:
    chunks = load_jsonl(input_path)
    texts = [chunk.get("embedding_text") or chunk.get("text", "") for chunk in chunks]
    vectors = encode_passages(texts, model_name=model_name, batch_size=batch_size)

    records = []
    for chunk, text, vector in zip(chunks, texts, vectors):
        records.append(
            {
                "chunk_id": chunk.get("chunk_id"),
                "vector": vector,
                "text": chunk.get("text"),
                "embedding_text": text,
                "metadata": metadata_for(chunk),
            }
        )

    save_jsonl(records, output_path)
    return {
        "input": str(input_path),
        "output": str(output_path),
        "records": len(records),
        "embedding_backend": "sentence-transformers",
        "model": model_name,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data_multisite_strict/kb/prototype_all_trusted.jsonl",
    )
    parser.add_argument(
        "--output",
        default="indexes/e5_base/index.jsonl",
    )
    parser.add_argument("--model", default=DEFAULT_E5_MODEL)
    parser.add_argument("--batch-size", type=int, default=16)
    args = parser.parse_args()
    summary = build_e5_index(args.input, args.output, args.model, args.batch_size)
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
