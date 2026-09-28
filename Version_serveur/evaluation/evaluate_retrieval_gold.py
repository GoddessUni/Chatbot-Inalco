from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAG_DIR = PROJECT_ROOT / "rag"
if str(RAG_DIR) not in sys.path:
    sys.path.insert(0, str(RAG_DIR))

from prompts import build_prompt  # noqa: E402
from retrieve_e5 import retrieve  # noqa: E402


def normalize_text(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(char for char in text if not unicodedata.combining(char))
    return " ".join(text.lower().split())


def normalize_url(value: object) -> str:
    raw = unquote(str(value or "").strip())
    if not raw:
        return ""
    parts = urlsplit(raw)
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, "", ""))


def evidence_key(evidence: dict) -> tuple[str, str, object, object]:
    return (
        normalize_url(evidence.get("source_url")),
        normalize_text(evidence.get("section_title")),
        evidence.get("page_start"),
        evidence.get("page_end"),
    )


def evidence_matches_hit(evidence: dict, hit: dict) -> bool:
    metadata = hit.get("metadata") or {}
    if normalize_url(evidence.get("source_url")) != normalize_url(
        metadata.get("source_url")
    ):
        return False

    expected_section = normalize_text(evidence.get("section_title"))
    actual_section = normalize_text(metadata.get("section_title"))
    if expected_section:
        if not actual_section:
            return False
        if expected_section not in actual_section and actual_section not in expected_section:
            return False

    expected_page = evidence.get("page_start")
    actual_start = metadata.get("page_start")
    actual_end = metadata.get("page_end") or actual_start
    if expected_page is not None:
        if actual_start is None or not (actual_start <= expected_page <= actual_end):
            return False
    return True


def load_dataset(path: Path, splits: set[str]) -> list[dict]:
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return [row for row in rows if not splits or row.get("split") in splits]


def unique_gold_evidence(row: dict) -> list[dict]:
    result = []
    seen = set()
    for evidence in row.get("gold_evidence") or []:
        key = evidence_key(evidence)
        if key in seen:
            continue
        seen.add(key)
        result.append(evidence)
    return result


def evaluate_row(row: dict, args: argparse.Namespace) -> dict:
    route_weight = 0.0 if args.method == "m1_semantic" else args.route_boost_weight
    hits = retrieve(
        row["question"],
        index_path=args.index,
        model_name=args.embedding_model,
        top_k=args.top_k,
        min_score=args.min_score,
        route_boost_weight=route_weight,
    )
    prompt = build_prompt(
        row["question"],
        hits,
        mode="standard",
        max_context_chars=args.max_context_chars,
        max_chunk_chars=args.max_chunk_chars,
        include_scores=False,
    )
    context_ranks = set(prompt.context_hit_ranks)
    gold = unique_gold_evidence(row)
    gold_ranks = []
    context_gold_ranks = []
    for evidence in gold:
        matched = [
            rank
            for rank, hit in enumerate(hits, start=1)
            if evidence_matches_hit(evidence, hit)
        ]
        first_rank = min(matched) if matched else None
        gold_ranks.append(first_rank)
        context_gold_ranks.append(
            min((rank for rank in matched if rank in context_ranks), default=None)
        )

    matched_retrieval = sum(rank is not None for rank in gold_ranks)
    matched_context = sum(rank is not None for rank in context_gold_ranks)
    gold_count = len(gold)
    expected_behavior = row.get("expected_behavior")
    context_has_gold = expected_behavior == "answer" and matched_context > 0

    return {
        "question_id": row.get("question_id"),
        "question": row.get("question"),
        "split": row.get("split"),
        "category": row.get("category"),
        "risk_level": row.get("risk_level"),
        "expected_behavior": expected_behavior,
        "method": args.method,
        "top_k": args.top_k,
        "route_boost_weight": route_weight,
        "top_score": hits[0].get("score") if hits else 0.0,
        "top_semantic_score": (
            hits[0].get("semantic_score", hits[0].get("score", 0.0)) if hits else 0.0
        ),
        "gold_evidence_count": gold_count,
        "gold_evidence_ranks": gold_ranks,
        "context_gold_evidence_ranks": context_gold_ranks,
        "retrieval_gold_recall": matched_retrieval / gold_count if gold_count else None,
        "context_gold_recall": matched_context / gold_count if gold_count else None,
        "first_gold_rank": min((rank for rank in gold_ranks if rank), default=None),
        "context_has_gold_evidence": context_has_gold,
        "context_source_ranks": prompt.context_hit_ranks,
        "context_chars": len(prompt.context),
        "hits": [
            {
                "rank": rank,
                "included_in_context": rank in context_ranks,
                "score": hit.get("score"),
                "semantic_score": hit.get("semantic_score", hit.get("score")),
                "source_url": (hit.get("metadata") or {}).get("source_url"),
                "title": (hit.get("metadata") or {}).get("title"),
                "section_title": (hit.get("metadata") or {}).get("section_title"),
                "page_start": (hit.get("metadata") or {}).get("page_start"),
                "page_end": (hit.get("metadata") or {}).get("page_end"),
            }
            for rank, hit in enumerate(hits, start=1)
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate retrieval and actual prompt context against gold evidence."
    )
    parser.add_argument("--dataset", required=True, type=Path)
    parser.add_argument("--index", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--splits", default="pilot,validation")
    parser.add_argument("--method", choices=("m1_semantic", "m2_rerank"), required=True)
    parser.add_argument("--embedding-model", default="intfloat/multilingual-e5-base")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    parser.add_argument("--route-boost-weight", type=float, default=1.0)
    parser.add_argument("--max-context-chars", type=int, default=6000)
    parser.add_argument("--max-chunk-chars", type=int, default=1000)
    args = parser.parse_args()

    splits = {item.strip() for item in args.splits.split(",") if item.strip()}
    dataset = load_dataset(args.dataset, splits)
    results = []
    for index, row in enumerate(dataset, start=1):
        print(f"[{index}/{len(dataset)}] {row.get('question_id')} {row.get('question')}")
        results.append(evaluate_row(row, args))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as file:
        for result in results:
            file.write(json.dumps(result, ensure_ascii=False) + "\n")

    answer_rows = [row for row in results if row["expected_behavior"] == "answer"]
    ranks = [row["first_gold_rank"] for row in answer_rows]
    summary = {
        "method": args.method,
        "splits": sorted(splits),
        "questions": len(results),
        "answer_questions": len(answer_rows),
        "hit_rate_at_k": (
            sum(rank is not None for rank in ranks) / len(ranks) if ranks else 0.0
        ),
        "mrr": (
            sum(1.0 / rank for rank in ranks if rank is not None) / len(ranks)
            if ranks
            else 0.0
        ),
        "context_hit_rate": (
            sum(row["context_has_gold_evidence"] for row in answer_rows)
            / len(answer_rows)
            if answer_rows
            else 0.0
        ),
        "mean_gold_recall_at_k": (
            sum(row["retrieval_gold_recall"] or 0.0 for row in answer_rows)
            / len(answer_rows)
            if answer_rows
            else 0.0
        ),
        "mean_context_gold_recall": (
            sum(row["context_gold_recall"] or 0.0 for row in answer_rows)
            / len(answer_rows)
            if answer_rows
            else 0.0
        ),
    }
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.summary.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
