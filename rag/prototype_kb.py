import argparse
import hashlib
import json
from pathlib import Path


def load_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def save_jsonl(records: list[dict], path: str | Path) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def load_optional_manual_faq(path: str | Path | None) -> list[dict]:
    if not path:
        return []

    faq_path = Path(path)
    if not faq_path.exists():
        raise FileNotFoundError(f"Manual FAQ file not found: {faq_path}")

    if faq_path.suffix.lower() == ".json":
        data = json.loads(faq_path.read_text(encoding="utf-8"))
        rows = data.get("records", data) if isinstance(data, dict) else data
    else:
        rows = load_jsonl(faq_path)

    records = []
    for index, row in enumerate(rows, start=1):
        question = (row.get("question") or "").strip()
        answer = (row.get("answer") or row.get("text") or "").strip()
        if not question or not answer:
            continue

        title = row.get("title") or "FAQ vérifiée manuellement"
        theme = row.get("theme") or "Général"
        source_url = row.get("source_url") or "manual://human-verified-faq"
        digest = hashlib.sha1(f"{question}\n{answer}".encode("utf-8")).hexdigest()[:16]
        text = f"Question: {question}\nRéponse: {answer}"

        records.append(
            {
                "chunk_id": row.get("chunk_id") or f"manual_faq_{digest}",
                "source_url": source_url,
                "source_urls": [source_url],
                "title": title,
                "section_title": row.get("section_title") or question,
                "text": text,
                "embedding_text": (
                    f"Titre: {title}\nThème: {theme}\n"
                    f"Question: {question}\nRéponse: {answer}"
                ),
                "theme": theme,
                "knowledge_type": row.get("knowledge_type") or "stable",
                "risk_level": row.get("risk_level") or "medium",
                "quality_status": "ready",
                "quality_flags": ["human_verified_faq"],
                "review_priority": None,
                "source_domain": "manual",
                "source_scope": "human_verified",
                "source_type": "human_verified_faq",
                "human_verified": True,
                "prototype_trusted": True,
                "curated_question": question,
                "curated_answer": answer,
                "manual_record_index": index,
            }
        )

    return records


def build_prototype_kb(
    input_path: str | Path,
    output_path: str | Path,
    manual_faq_path: str | Path | None = None,
) -> dict:
    records = []
    for chunk in load_jsonl(input_path):
        record = dict(chunk)
        record["prototype_trusted"] = True
        record["prototype_note"] = (
            "For prototype evaluation only: chunks requiring review are treated "
            "as verified, while their quality metadata is preserved."
        )
        records.append(record)

    manual_records = load_optional_manual_faq(manual_faq_path)
    records.extend(manual_records)

    save_jsonl(records, output_path)
    return {
        "input": str(input_path),
        "output": str(output_path),
        "records": len(records),
        "manual_faq_records": len(manual_records),
        "review_records_treated_as_trusted": sum(
            record.get("quality_status") == "review" for record in records
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data_multisite_strict/kb/all_indexable_with_embedding_text.jsonl",
    )
    parser.add_argument(
        "--output",
        default="data_multisite_strict/kb/prototype_all_trusted.jsonl",
    )
    parser.add_argument(
        "--manual-faq",
        default=None,
        help=(
            "Optional JSON/JSONL file with human-verified question/answer records "
            "to add to the prototype KB."
        ),
    )
    args = parser.parse_args()
    summary = build_prototype_kb(args.input, args.output, args.manual_faq)
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
