#!/usr/bin/env python3
"""Generate reproducible tables and figures from a frozen Inalco test run."""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


METHODS = (
    "m0_llm_only",
    "m1_rag_simple",
    "m2_rag_rerank",
    "m3_rag_threshold",
    "m4_rag_abstention",
)
LABELS = ("answer", "clarify", "abstain")
DISPLAY = {
    "m0_llm_only": "M0 LLM seul",
    "m1_rag_simple": "M1 RAG simple",
    "m2_rag_rerank": "M2 RAG + rerank",
    "m3_rag_threshold": "M3 RAG + seuil",
    "m4_rag_abstention": "M4 RAG + abstention",
}
COLORS = {
    "m0_llm_only": "#7f8c8d",
    "m1_rag_simple": "#2471a3",
    "m2_rag_rerank": "#17a589",
    "m3_rag_threshold": "#d68910",
    "m4_rag_abstention": "#a93226",
}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def predicted_behavior(row: dict) -> str:
    if row.get("clarify"):
        return "clarify"
    if row.get("abstain"):
        return "abstain"
    return "answer"


def safe_div(numerator: float, denominator: float) -> float:
    return numerator / denominator if denominator else 0.0


def wilson_interval(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if not total:
        return 0.0, 0.0
    p = successes / total
    denominator = 1 + z * z / total
    centre = (p + z * z / (2 * total)) / denominator
    margin = (
        z
        * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total))
        / denominator
    )
    return max(0.0, centre - margin), min(1.0, centre + margin)


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def behavior_rows(run_dir: Path) -> tuple[list[dict], dict[str, list[dict]]]:
    table = []
    raw = {}
    for method in METHODS:
        answers = load_jsonl(run_dir / f"{method}.jsonl")
        raw[method] = answers
        summary = load_json(run_dir / f"{method}_behavior.json")
        expected = Counter(row.get("expected_behavior") for row in answers)
        predicted = Counter(predicted_behavior(row) for row in answers)
        answer_support = expected["answer"]
        abstain_support = expected["abstain"]
        clarify_support = expected["clarify"]
        answer_correct = sum(
            row.get("expected_behavior") == "answer"
            and predicted_behavior(row) == "answer"
            for row in answers
        )
        correct_abstentions = sum(
            row.get("expected_behavior") == "abstain"
            and predicted_behavior(row) == "abstain"
            for row in answers
        )
        correct_clarifications = sum(
            row.get("expected_behavior") == "clarify"
            and predicted_behavior(row) == "clarify"
            for row in answers
        )
        unsafe_answers = sum(
            row.get("expected_behavior") == "abstain"
            and predicted_behavior(row) == "answer"
            for row in answers
        )
        over_abstentions = sum(
            row.get("expected_behavior") == "answer"
            and predicted_behavior(row) == "abstain"
            for row in answers
        )
        coverage_low, coverage_high = wilson_interval(predicted["answer"], len(answers))
        unsafe_low, unsafe_high = wilson_interval(unsafe_answers, abstain_support)
        table.append(
            {
                "method": method,
                "display_name": DISPLAY[method],
                "records": len(answers),
                "accuracy": summary["accuracy"],
                "macro_f1": summary["macro_f1"],
                "answer_coverage": safe_div(predicted["answer"], len(answers)),
                "answer_coverage_ci_low": coverage_low,
                "answer_coverage_ci_high": coverage_high,
                "answer_recall": safe_div(answer_correct, answer_support),
                "clarification_recall": safe_div(correct_clarifications, clarify_support),
                "abstention_recall": safe_div(correct_abstentions, abstain_support),
                "unsafe_answer_rate": safe_div(unsafe_answers, abstain_support),
                "unsafe_answer_ci_low": unsafe_low,
                "unsafe_answer_ci_high": unsafe_high,
                "over_abstention_rate": safe_div(over_abstentions, answer_support),
                "predicted_answer": predicted["answer"],
                "predicted_clarify": predicted["clarify"],
                "predicted_abstain": predicted["abstain"],
                "errors": sum(bool(row.get("error")) for row in answers),
            }
        )
    return table, raw


def retrieval_rows(run_dir: Path) -> list[dict]:
    result = []
    for stem, display in (
        ("m1_retrieval_summary", "M1 semantic"),
        ("m2_retrieval_summary", "M2 rerank"),
    ):
        row = load_json(run_dir / f"{stem}.json")
        result.append(
            {
                "method": row["method"],
                "display_name": display,
                "answer_questions": row["answer_questions"],
                "hit_rate_at_k": row["hit_rate_at_k"],
                "mrr": row["mrr"],
                "context_hit_rate": row["context_hit_rate"],
                "mean_gold_recall_at_k": row["mean_gold_recall_at_k"],
                "mean_context_gold_recall": row["mean_context_gold_recall"],
            }
        )
    return result


def plot_retrieval(rows: list[dict], output: Path) -> None:
    metrics = (
        ("hit_rate_at_k", "Hit@5"),
        ("mrr", "MRR"),
        ("mean_gold_recall_at_k", "Gold recall@5"),
        ("mean_context_gold_recall", "Context gold recall"),
    )
    x = list(range(len(metrics)))
    width = 0.34
    fig, ax = plt.subplots(figsize=(9, 5.2))
    for index, row in enumerate(rows):
        offsets = [value + (index - 0.5) * width for value in x]
        values = [row[key] for key, _ in metrics]
        bars = ax.bar(offsets, values, width, label=row["display_name"])
        ax.bar_label(bars, labels=[f"{value:.3f}" for value in values], padding=3, fontsize=8)
    ax.set_ylim(0, 1.08)
    ax.set_ylabel("Score")
    ax.set_xticks(x, [label for _, label in metrics])
    ax.set_title("Retrieval performance on the frozen test set")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(output, dpi=220)
    plt.close(fig)


def plot_behavior(rows: list[dict], output: Path) -> None:
    metrics = (
        ("accuracy", "Accuracy"),
        ("macro_f1", "Macro-F1"),
        ("answer_recall", "Answer recall"),
        ("abstention_recall", "Abstention recall"),
        ("unsafe_answer_rate", "Unsafe answer rate"),
        ("over_abstention_rate", "Over-abstention"),
    )
    fig, axes = plt.subplots(2, 3, figsize=(13, 7.5), sharey=True)
    names = [row["display_name"] for row in rows]
    colors = [COLORS[row["method"]] for row in rows]
    for ax, (key, title) in zip(axes.flat, metrics):
        values = [row[key] for row in rows]
        bars = ax.bar(range(len(rows)), values, color=colors)
        ax.bar_label(bars, labels=[f"{value:.2f}" for value in values], padding=2, fontsize=7)
        ax.set_title(title)
        ax.set_ylim(0, 1.12)
        ax.set_xticks(range(len(rows)), [name.split()[0] for name in names])
        ax.grid(axis="y", alpha=0.2)
    fig.suptitle("Behavior and safety metrics on the frozen test set", fontsize=14)
    fig.tight_layout()
    fig.savefig(output, dpi=220)
    plt.close(fig)


def plot_confusions(run_dir: Path, output: Path) -> None:
    fig, axes = plt.subplots(1, 5, figsize=(16, 3.7), sharex=True, sharey=True)
    image = None
    for ax, method in zip(axes, METHODS):
        summary = load_json(run_dir / f"{method}_behavior.json")
        confusion = summary["confusion"]
        matrix = [[confusion[actual][predicted] for predicted in LABELS] for actual in LABELS]
        image = ax.imshow(matrix, cmap="Blues", vmin=0, vmax=max(max(row) for row in matrix))
        for row_index, row in enumerate(matrix):
            for column_index, value in enumerate(row):
                ax.text(column_index, row_index, value, ha="center", va="center", fontsize=9)
        ax.set_title(method.split("_")[0].upper())
        ax.set_xticks(range(3), ["A", "C", "R"])
        ax.set_yticks(range(3), ["A", "C", "R"])
        ax.set_xlabel("Predicted")
    axes[0].set_ylabel("Expected")
    fig.suptitle("Behavior confusion matrices (A=answer, C=clarify, R=abstain)")
    if image is not None:
        fig.colorbar(image, ax=axes, shrink=0.75, pad=0.02)
    fig.subplots_adjust(left=0.05, right=0.94, bottom=0.16, top=0.78, wspace=0.28)
    fig.savefig(output, dpi=220)
    plt.close(fig)


def plot_safety_coverage(rows: list[dict], output: Path) -> None:
    fig, ax = plt.subplots(figsize=(7.5, 5.8))
    for row in rows:
        coverage = row["answer_coverage"]
        safety = 1 - row["unsafe_answer_rate"]
        ax.scatter(coverage, safety, s=110, color=COLORS[row["method"]], zorder=3)
        ax.annotate(
            row["method"].split("_")[0].upper(),
            (coverage, safety),
            xytext=(7, 5),
            textcoords="offset points",
        )
    ax.set_xlim(-0.03, 1.05)
    ax.set_ylim(-0.03, 1.05)
    ax.set_xlabel("Answer coverage")
    ax.set_ylabel("Safety = 1 - unsafe answer rate")
    ax.set_title("Safety-coverage trade-off")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(output, dpi=220)
    plt.close(fig)


def plot_threshold_diagnostic(run_dir: Path, output: Path) -> None:
    retrieval = load_jsonl(run_dir / "m1_retrieval.jsonl")
    m3 = {row["question_id"]: row for row in load_jsonl(run_dir / "m3_rag_threshold.jsonl")}
    answer_rows = [row for row in retrieval if row.get("expected_behavior") == "answer"]
    with_gold = [row["top_semantic_score"] for row in answer_rows if row.get("context_has_gold_evidence")]
    without_gold = [row["top_semantic_score"] for row in answer_rows if not row.get("context_has_gold_evidence")]
    threshold_values = {
        row.get("semantic_threshold")
        for row in m3.values()
        if row.get("semantic_threshold") is not None
    }
    threshold = next(iter(threshold_values), None)
    fig, ax = plt.subplots(figsize=(8, 5.3))
    bins = 14
    ax.hist(with_gold, bins=bins, alpha=0.68, label="Gold evidence in context", color="#2471a3")
    ax.hist(without_gold, bins=bins, alpha=0.78, label="No gold evidence in context", color="#c0392b")
    if threshold is not None:
        ax.axvline(threshold, color="#17202a", linestyle="--", linewidth=2, label=f"Frozen threshold {threshold:.6f}")
    ax.set_xlabel("Top semantic score")
    ax.set_ylabel("Number of answerable questions")
    ax.set_title("Semantic score versus evidence sufficiency")
    ax.legend(frameon=False)
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(output, dpi=220)
    plt.close(fig)


def category_rows(raw: dict[str, list[dict]]) -> list[dict]:
    rows = []
    for method, answers in raw.items():
        grouped = defaultdict(list)
        for row in answers:
            grouped[row.get("category") or "Unspecified"].append(row)
        for category, items in sorted(grouped.items()):
            correct = sum(
                predicted_behavior(row) == row.get("expected_behavior") for row in items
            )
            rows.append(
                {
                    "method": method,
                    "category": category,
                    "questions": len(items),
                    "behavior_accuracy": safe_div(correct, len(items)),
                }
            )
    return rows


def write_markdown(output: Path, behavior: list[dict], retrieval: list[dict]) -> None:
    lines = [
        "# Frozen Test Report",
        "",
        "## Retrieval",
        "",
        "| Method | Hit@5 | MRR | Gold recall@5 | Context gold recall |",
        "|---|---:|---:|---:|---:|",
    ]
    for row in retrieval:
        lines.append(
            f"| {row['display_name']} | {row['hit_rate_at_k']:.3f} | "
            f"{row['mrr']:.3f} | {row['mean_gold_recall_at_k']:.3f} | "
            f"{row['mean_context_gold_recall']:.3f} |"
        )
    lines.extend(
        [
            "",
            "## Behavior And Safety",
            "",
            "| Method | Accuracy | Macro-F1 | Coverage | Answer recall | Clarify recall | Abstain recall | Unsafe answer | Over-abstention |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for row in behavior:
        lines.append(
            f"| {row['display_name']} | {row['accuracy']:.3f} | {row['macro_f1']:.3f} | "
            f"{row['answer_coverage']:.3f} | {row['answer_recall']:.3f} | "
            f"{row['clarification_recall']:.3f} | {row['abstention_recall']:.3f} | "
            f"{row['unsafe_answer_rate']:.3f} | {row['over_abstention_rate']:.3f} |"
        )
    lines.extend(
        [
            "",
            "## Scope",
            "",
            "These tables evaluate retrieval and answer/clarify/abstain behavior. ",
            "They do not measure factual faithfulness, unsupported claims, or citation correctness. ",
            "Those generation-quality measures require human annotation or a separately validated judge.",
            "",
        ]
    )
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    output_dir = (args.output_dir or run_dir / "thesis_report").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    behavior, raw = behavior_rows(run_dir)
    retrieval = retrieval_rows(run_dir)
    categories = category_rows(raw)
    write_csv(output_dir / "behavior_metrics.csv", behavior, list(behavior[0]))
    write_csv(output_dir / "retrieval_metrics.csv", retrieval, list(retrieval[0]))
    write_csv(
        output_dir / "behavior_by_category.csv",
        categories,
        ["method", "category", "questions", "behavior_accuracy"],
    )
    write_markdown(output_dir / "summary_tables.md", behavior, retrieval)
    plot_retrieval(retrieval, output_dir / "retrieval_metrics.png")
    plot_behavior(behavior, output_dir / "behavior_metrics.png")
    plot_confusions(run_dir, output_dir / "confusion_matrices.png")
    plot_safety_coverage(behavior, output_dir / "safety_coverage.png")
    plot_threshold_diagnostic(run_dir, output_dir / "threshold_diagnostic.png")
    print(f"Report written to: {output_dir}")


if __name__ == "__main__":
    main()
