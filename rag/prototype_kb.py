import argparse
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


def build_prototype_kb(input_path: str | Path, output_path: str | Path) -> dict:
    records = []
    for chunk in load_jsonl(input_path):
        record = dict(chunk)
        record["prototype_trusted"] = True
        record["prototype_note"] = (
            "For prototype evaluation only: chunks requiring review are treated "
            "as verified, while their quality metadata is preserved."
        )
        records.append(record)

    save_jsonl(records, output_path)
    return {
        "input": str(input_path),
        "output": str(output_path),
        "records": len(records),
        "review_records_treated_as_trusted": sum(
            record.get("quality_status") == "review" for record in records
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="data/kb/all_indexable_with_embedding_text.jsonl",
    )
    parser.add_argument(
        "--output",
        default="data/kb/prototype_all_trusted.jsonl",
    )
    args = parser.parse_args()
    summary = build_prototype_kb(args.input, args.output)
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
