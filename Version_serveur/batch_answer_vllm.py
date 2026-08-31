from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Any


DEFAULT_PROJECT_ROOT = Path(__file__).resolve().parent
DEFAULT_QUESTIONS = DEFAULT_PROJECT_ROOT / "questions_probables.txt"
DEFAULT_INDEX = DEFAULT_PROJECT_ROOT / "indexes/e5_plus_0710/index.jsonl"
DEFAULT_OUTPUT_JSONL = DEFAULT_PROJECT_ROOT / "evaluation/answers_vllm.jsonl"
DEFAULT_OUTPUT_MD = DEFAULT_PROJECT_ROOT / "evaluation/answers_vllm.md"


def load_rag_module(project_root: Path):
    rag_dir = project_root / "rag"
    if not rag_dir.exists():
        raise FileNotFoundError(f"RAG directory not found: {rag_dir}")
    sys.path.insert(0, str(rag_dir))
    from answer_vllm import answer_question

    return answer_question


def read_questions(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_done_questions(path: Path) -> set[str]:
    if not path.exists():
        return set()
    done = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            question = json.loads(line).get("question")
        except json.JSONDecodeError:
            continue
        if question:
            done.add(question)
    return done


def append_jsonl(record: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record, ensure_ascii=False) + "\n")


def render_markdown(records: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# Reponses du prototype RAG + vLLM", ""]
    for record in records:
        lines.extend([f"## Q{record['question_id']}. {record['question']}", ""])
        if record.get("error"):
            lines.extend(["**Erreur :**", "", record["error"], ""])
            continue
        lines.extend(["**Reponse :**", "", record.get("answer", ""), "", "**Sources recuperees :**", ""])
        for source in record.get("sources", []):
            lines.append(
                f"- [{source.get('rank')}] {source.get('title') or 'Sans titre'} / "
                f"{source.get('section_title') or 'Sans section'} "
                f"(score={source.get('score')}, semantic={source.get('semantic_score')})  "
                f"{source.get('source_url') or ''}"
            )
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def build_answer_args(args: argparse.Namespace, question: str) -> SimpleNamespace:
    return SimpleNamespace(
        question=question,
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
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--output-jsonl", type=Path, default=DEFAULT_OUTPUT_JSONL)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUTPUT_MD)
    parser.add_argument("--model", default="mistralai/Ministral-8B-Instruct-2410")
    parser.add_argument("--embedding-model", default="intfloat/multilingual-e5-base")
    parser.add_argument("--api-url", default="http://127.0.0.1:8000/v1/chat/completions")
    parser.add_argument("--top-k", type=int, default=3)
    parser.add_argument("--min-score", type=float, default=0.0)
    parser.add_argument("--route-boost-weight", type=float, default=1.0)
    parser.add_argument("--max-context-chars", type=int, default=3500)
    parser.add_argument("--max-chunk-chars", type=int, default=900)
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--top-p", type=float, default=0.8)
    parser.add_argument("--num-predict", type=int, default=350)
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

    answer_question = load_rag_module(args.project_root)
    questions = read_questions(args.questions)
    selected = questions[args.start - 1 :]
    if args.limit is not None:
        selected = selected[: args.limit]

    done = load_done_questions(args.output_jsonl) if args.resume else set()
    new_records = []
    for offset, question in enumerate(selected, start=args.start):
        if question in done:
            print(f"[{offset}/{len(questions)}] skipped: {question}")
            continue
        print(f"[{offset}/{len(questions)}] answering: {question}")
        started = time.time()
        record = {
            "question_id": offset,
            "question": question,
            "model": args.model,
            "backend": "vllm",
            "index": str(args.index),
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
