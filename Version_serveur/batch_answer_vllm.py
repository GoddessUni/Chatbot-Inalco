from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_QUESTIONS = DEFAULT_PROJECT_ROOT / "questions_probables.txt"
CURRENT_INDEX = DEFAULT_PROJECT_ROOT / "indexes/current/index.jsonl"
LEGACY_INDEX = DEFAULT_PROJECT_ROOT / "indexes/e5_plus_0710/index.jsonl"
DEFAULT_INDEX = Path(
    os.getenv(
        "RAG_INDEX_PATH",
        str(CURRENT_INDEX if CURRENT_INDEX.exists() else LEGACY_INDEX),
    )
)
DEFAULT_MODEL = os.getenv(
    "VLLM_MODEL", "mistralai/Ministral-8B-Instruct-2410"
)
DEFAULT_EMBEDDING_MODEL = os.getenv(
    "RAG_EMBEDDING_MODEL", "intfloat/multilingual-e5-base"
)
DEFAULT_API_URL = os.getenv(
    "VLLM_API_URL", "http://127.0.0.1:8000/v1/chat/completions"
)
DEFAULT_OUTPUT_JSONL = DEFAULT_PROJECT_ROOT / "evaluation/answers_vllm.jsonl"
DEFAULT_OUTPUT_MD = DEFAULT_PROJECT_ROOT / "evaluation/answers_vllm.md"

EXPERIMENT_METHODS = (
    "m0_llm_only",
    "m1_rag_simple",
    "m2_rag_rerank",
    "m3_rag_threshold",
    "m4_rag_abstention",
)


def load_rag_module(project_root: Path):
    rag_dir = project_root / "rag"
    if not rag_dir.exists():
        raise FileNotFoundError(f"RAG directory not found: {rag_dir}")
    sys.path.insert(0, str(rag_dir))
    from answer_vllm import answer_question

    return answer_question


def read_question_records(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".jsonl":
        rows = [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    elif suffix == ".json":
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload.get("records", payload) if isinstance(payload, dict) else payload
    else:
        rows = [
            {"question_id": index, "question": line.strip()}
            for index, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), start=1
            )
            if line.strip()
        ]

    records = []
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            row = {"question": str(row)}
        question = (row.get("question") or "").strip()
        if not question:
            continue
        records.append(
            {
                "question_id": row.get("question_id", row.get("id", index)),
                "question": question,
                "split": row.get("split"),
                "category": row.get("category"),
                "risk_level": row.get("risk_level"),
                "expected_behavior": row.get("expected_behavior"),
                "gold_facts": row.get("gold_facts", []),
                "gold_evidence": row.get("gold_evidence", []),
            }
        )
    return records


def load_done_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    done = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        identifier = record.get("question_id") or record.get("question")
        if identifier is not None:
            done.add(str(identifier))
    return done


def append_jsonl(record: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def sha256_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def render_markdown(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Reponses du prototype Inalco + vLLM", ""]
    for record in records:
        identifier = str(record["question_id"])
        heading = identifier if identifier.lower().startswith("q") else f"Q{identifier}"
        lines.extend([f"## {heading}. {record['question']}", ""])
        lines.extend(
            [
                f"**Methode :** `{record.get('method', 'unknown')}`  ",
                f"**Experience :** `{record.get('experiment_id', 'unknown')}`  ",
                f"**Mode de recuperation :** `{record.get('retrieval_mode', 'unknown')}`  ",
                f"**Mode de prompt :** `{record.get('prompt_mode', 'unknown')}`",
                f"**Split :** `{record.get('split') or 'non précisé'}`  ",
                f"**Comportement attendu :** `{record.get('expected_behavior') or 'non précisé'}`  ",
                f"**Abstention produite :** `{record.get('abstain', False)}`",
                f"**Clarification produite :** `{record.get('clarify', False)}`  ",
                f"**Sources dans le contexte :** `{record.get('context_source_count', 0)}`  ",
                f"**Taille du contexte :** `{record.get('context_chars', 0)} caractères`",
                "",
            ]
        )
        if record.get("error"):
            lines.extend(["**Erreur :**", "", record["error"], ""])
            continue
        lines.extend(["**Reponse :**", "", record.get("answer", ""), "", "**Sources recuperees :**", ""])
        for source in record.get("sources", []):
            context_label = "oui" if source.get("included_in_context") else "non"
            lines.append(
                f"- [{source.get('rank')}] {source.get('title') or 'Sans titre'} / "
                f"{source.get('section_title') or 'Sans section'} "
                f"(pages={source.get('page_start') or 'n/a'}"
                f"-{source.get('page_end') or source.get('page_start') or 'n/a'}, "
                f"score={source.get('score')}, semantic={source.get('semantic_score')}, "
                f"dans_contexte={context_label})  "
                f"{source.get('source_url') or ''}"
            )
        gold_facts = record.get("gold_facts") or []
        if gold_facts:
            lines.extend(["", "**Faits de référence (non transmis au modèle) :**", ""])
            for fact in gold_facts:
                fact_text = fact.get("text", "") if isinstance(fact, dict) else str(fact)
                lines.append(f"- {fact_text}")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def build_answer_args(args: argparse.Namespace, question: str) -> SimpleNamespace:
    return SimpleNamespace(
        question=question,
        method=args.method,
        experiment_id=args.experiment_id or args.method,
        index=str(args.index),
        embedding_model=args.embedding_model,
        model=args.model,
        api_url=args.api_url,
        top_k=args.top_k,
        min_score=args.min_score,
        route_boost_weight=args.route_boost_weight,
        max_context_chars=args.max_context_chars,
        max_chunk_chars=args.max_chunk_chars,
        temperature=args.temperature,
        top_p=args.top_p,
        num_predict=args.num_predict,
        seed=args.seed,
        timeout=args.timeout,
        confidence_threshold=args.confidence_threshold,
        semantic_threshold=args.semantic_threshold,
        hide_scores=args.hide_scores,
        dry_run=args.dry_run,
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Batch evaluation for the Inalco RAG chatbot with vLLM."
    )
    parser.add_argument("--project-root", type=Path, default=DEFAULT_PROJECT_ROOT)
    parser.add_argument(
        "--method",
        choices=EXPERIMENT_METHODS,
        default="m2_rag_rerank",
    )
    parser.add_argument("--experiment-id", default=None)
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument(
        "--split",
        choices=("pilot", "validation", "test"),
        default=None,
        help="Filter a JSON/JSONL evaluation dataset by split.",
    )
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--output-jsonl", type=Path, default=DEFAULT_OUTPUT_JSONL)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--embedding-model", default=DEFAULT_EMBEDDING_MODEL)
    parser.add_argument("--api-url", default=DEFAULT_API_URL)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    parser.add_argument("--route-boost-weight", type=float, default=1.0)
    parser.add_argument("--max-context-chars", type=int, default=6000)
    parser.add_argument("--max-chunk-chars", type=int, default=1000)
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--top-p", type=float, default=0.8)
    parser.add_argument("--num-predict", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--confidence-threshold", type=float, default=None)
    parser.add_argument("--semantic-threshold", type=float, default=None)
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--sleep", type=float, default=0.0)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--hide-scores", action="store_true")
    args = parser.parse_args()

    if (
        args.method in {"m3_rag_threshold", "m4_rag_abstention"}
        and args.confidence_threshold is None
        and args.semantic_threshold is None
    ):
        parser.error(
            f"{args.method} requires --confidence-threshold and/or "
            "--semantic-threshold calibrated on the validation set"
        )

    answer_question = load_rag_module(args.project_root)
    index_sha256 = sha256_file(args.index)
    questions = read_question_records(args.questions)
    if args.split:
        questions = [record for record in questions if record.get("split") == args.split]
    selected = questions[args.start - 1 :]
    if args.limit is not None:
        selected = selected[: args.limit]

    done = load_done_ids(args.output_jsonl) if args.resume else set()
    new_records = []
    for offset, item in enumerate(selected, start=args.start):
        question_id = item["question_id"]
        question = item["question"]
        if str(question_id) in done:
            print(f"[{offset}/{len(questions)}] skipped: {question_id} {question}")
            continue
        print(f"[{offset}/{len(questions)}] answering: {question_id} {question}")
        started = time.time()
        record = {
            "question_id": question_id,
            "question": question,
            "split": item.get("split"),
            "category": item.get("category"),
            "risk_level": item.get("risk_level"),
            "expected_behavior": item.get("expected_behavior"),
            "gold_facts": item.get("gold_facts", []),
            "gold_evidence": item.get("gold_evidence", []),
            "method": args.method,
            "experiment_id": args.experiment_id or args.method,
            "model": args.model,
            "backend": "vllm",
            "index": str(args.index),
            "index_sha256": index_sha256,
            "top_k": args.top_k,
            "route_boost_weight_requested": args.route_boost_weight,
            "confidence_threshold": args.confidence_threshold,
            "semantic_threshold": args.semantic_threshold,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "seed": args.seed,
        }
        try:
            record.update(answer_question(build_answer_args(args, question)))
        except Exception as exc:
            record["error"] = f"{type(exc).__name__}: {exc}"
        record["elapsed_seconds"] = round(time.time() - started, 2)
        append_jsonl(record, args.output_jsonl)
        new_records.append(record)
        if args.sleep:
            time.sleep(args.sleep)

    all_records = []
    if args.output_jsonl.exists():
        all_records = [
            json.loads(line)
            for line in args.output_jsonl.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
    render_markdown(all_records, args.output_md)
    print(f"\nJSONL: {args.output_jsonl}")
    print(f"Markdown: {args.output_md}")
    print(f"New records: {len(new_records)}")


if __name__ == "__main__":
    main()
