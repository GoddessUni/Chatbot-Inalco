from __future__ import annotations

import argparse
import json
import unicodedata
from collections import Counter
from pathlib import Path


LABELS = ("answer", "clarify", "abstain")


def actual_behavior(row: dict) -> str:
    if row.get("clarify"):
        return "clarify"
    if row.get("abstain"):
        return "abstain"
    if "clarify" not in row:
        answer = unicodedata.normalize("NFKD", row.get("answer") or "")
        answer = "".join(
            char for char in answer if not unicodedata.combining(char)
        ).lower()
        if any(
            marker in answer
            for marker in (
                "pouvez-vous preciser",
                "veuillez preciser",
                "merci de preciser",
            )
        ):
            return "clarify"
    return "answer"


def safe_div(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 0.0


def main() -> None:
    parser = argparse.ArgumentParser(description="Score answer/clarify/abstain behavior.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    rows = [
        json.loads(line)
        for line in args.input.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    pairs = [
        (row.get("expected_behavior"), actual_behavior(row))
        for row in rows
        if row.get("expected_behavior") in LABELS and not row.get("error")
    ]
    confusion = Counter(pairs)
    per_label = {}
    for label in LABELS:
        tp = confusion[(label, label)]
        fp = sum(confusion[(expected, label)] for expected in LABELS if expected != label)
        fn = sum(confusion[(label, actual)] for actual in LABELS if actual != label)
        precision = safe_div(tp, tp + fp)
        recall = safe_div(tp, tp + fn)
        per_label[label] = {
            "precision": precision,
            "recall": recall,
            "f1": safe_div(2 * precision * recall, precision + recall),
            "support": sum(confusion[(label, actual)] for actual in LABELS),
        }

    report = {
        "input": str(args.input),
        "records": len(rows),
        "scored_records": len(pairs),
        "accuracy": safe_div(sum(expected == actual for expected, actual in pairs), len(pairs)),
        "macro_f1": sum(per_label[label]["f1"] for label in LABELS) / len(LABELS),
        "per_label": per_label,
        "confusion": {
            expected: {actual: confusion[(expected, actual)] for actual in LABELS}
            for expected in LABELS
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
