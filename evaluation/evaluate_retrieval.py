import argparse
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAG_DIR = PROJECT_ROOT / "rag"
if str(RAG_DIR) not in sys.path:
    sys.path.insert(0, str(RAG_DIR))

from retrieve_e5 import retrieve


def load_questions(path: str | Path) -> list[dict]:
    question_path = Path(path)
    records = []

    if question_path.suffix.lower() == ".json":
        data = json.loads(question_path.read_text(encoding="utf-8"))
        rows = data.get("records", data) if isinstance(data, dict) else data
    elif question_path.suffix.lower() == ".jsonl":
        rows = [
            json.loads(line)
            for line in question_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    else:
        rows = [
            {"question": line.strip()}
            for line in question_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    for index, row in enumerate(rows, start=1):
        question = row["question"] if isinstance(row, dict) else str(row)
        records.append(
            {
                "id": row.get("id", index) if isinstance(row, dict) else index,
                "theme": row.get("theme") if isinstance(row, dict) else None,
                "question": question.strip(),
                "expected_source_contains": (
                    row.get("expected_source_contains", [])
                    if isinstance(row, dict)
                    else []
                ),
            }
        )

    return [record for record in records if record["question"]]


def source_matches(hit: dict, expected_parts: list[str]) -> bool:
    if not expected_parts:
        return False
    source = (hit.get("metadata", {}).get("source_url") or "").lower()
    return any(part.lower() in source for part in expected_parts)


def status_for(top_score: float, expected_found: bool) -> str:
    if expected_found:
        return "expected_source_found"
    if top_score >= 0.82:
        return "probable"
    if top_score >= 0.72:
        return "partial"
    return "weak"


def evaluate(
    questions_path: str | Path,
    index_path: str | Path,
    output_path: str | Path,
    top_k: int,
    min_score: float,
) -> dict:
    questions = load_questions(questions_path)
    results = []

    for item in questions:
        hits = retrieve(
            item["question"],
            index_path=index_path,
            top_k=top_k,
            min_score=min_score,
        )
        expected_found = any(
            source_matches(hit, item["expected_source_contains"]) for hit in hits
        )
        top_score = hits[0]["score"] if hits else 0.0
        results.append(
            {
                **item,
                "status": status_for(top_score, expected_found),
                "top_score": top_score,
                "hits": [
                    {
                        "rank": rank,
                        "score": hit["score"],
                        "title": hit["metadata"].get("title"),
                        "section_title": hit["metadata"].get("section_title"),
                        "source_url": hit["metadata"].get("source_url"),
                        "source_type": hit["metadata"].get("source_type"),
                        "text_preview": (hit.get("text") or "").replace("\n", " ")[:350],
                    }
                    for rank, hit in enumerate(hits, start=1)
                ],
            }
        )

    summary = {
        "questions": len(results),
        "statuses": {
            status: sum(1 for result in results if result["status"] == status)
            for status in sorted({result["status"] for result in results})
        },
        "results": results,
    }

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", required=True)
    parser.add_argument("--index", default="indexes/e5_base/index.jsonl")
    parser.add_argument("--output", default="evaluation/retrieval_eval.json")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    args = parser.parse_args()

    summary = evaluate(
        args.questions,
        args.index,
        args.output,
        args.top_k,
        args.min_score,
    )
    print(f"Questions: {summary['questions']}")
    for status, count in summary["statuses"].items():
        print(f"{status}: {count}")
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
