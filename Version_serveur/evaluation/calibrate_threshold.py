from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def safe_div(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 0.0


def metrics_for(rows: list[dict], threshold: float) -> dict:
    tp = tn = fp = fn = 0
    for row in rows:
        sufficient = bool(row["context_has_gold_evidence"])
        passes = float(row["top_semantic_score"]) >= threshold
        if sufficient and passes:
            tp += 1
        elif sufficient:
            fn += 1
        elif passes:
            fp += 1
        else:
            tn += 1

    precision = safe_div(tp, tp + fp)
    recall = safe_div(tp, tp + fn)
    specificity = safe_div(tn, tn + fp)
    return {
        "threshold": threshold,
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "precision": precision,
        "recall": recall,
        "f1": safe_div(2 * precision * recall, precision + recall),
        "specificity": specificity,
        "balanced_accuracy": (recall + specificity) / 2,
        "unsafe_answer_rate": safe_div(fp, fp + tn),
        "over_abstention_rate": safe_div(fn, tp + fn),
        "answer_coverage": safe_div(tp + fp, len(rows)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Calibrate a semantic abstention threshold on development data."
    )
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-json", required=True, type=Path)
    parser.add_argument("--output-csv", required=True, type=Path)
    parser.add_argument("--max-unsafe-rate", type=float, default=0.20)
    args = parser.parse_args()

    all_rows = [
        json.loads(line)
        for line in args.input.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    rows = [row for row in all_rows if row.get("expected_behavior") != "clarify"]
    scores = sorted({float(row["top_semantic_score"]) for row in rows})
    thresholds = sorted({0.0, 1.0, *scores, *(min(1.0, score + 1e-6) for score in scores)})
    curve = [metrics_for(rows, threshold) for threshold in thresholds]

    safest = [
        item for item in curve if item["unsafe_answer_rate"] <= args.max_unsafe_rate
    ]
    candidates = safest or curve
    recommended = max(
        candidates,
        key=lambda item: (
            item["balanced_accuracy"],
            item["f1"],
            item["answer_coverage"],
            -item["threshold"],
        ),
    )

    report = {
        "input": str(args.input),
        "records_total": len(all_rows),
        "records_used": len(rows),
        "clarify_records_excluded": len(all_rows) - len(rows),
        "sufficient_context_records": sum(
            bool(row["context_has_gold_evidence"]) for row in rows
        ),
        "insufficient_context_records": sum(
            not bool(row["context_has_gold_evidence"]) for row in rows
        ),
        "max_unsafe_rate": args.max_unsafe_rate,
        "recommended": recommended,
        "curve": curve,
        "warning": (
            "The threshold is a development-set estimate. Keep the test split untouched "
            "and report coverage together with abstention safety."
        ),
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(curve[0]))
        writer.writeheader()
        writer.writerows(curve)

    print(json.dumps({key: value for key, value in report.items() if key != "curve"}, indent=2))


if __name__ == "__main__":
    main()
