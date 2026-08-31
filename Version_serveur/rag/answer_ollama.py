from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from prompts import build_prompt, should_abstain
from retrieve_e5 import retrieve


DEFAULT_OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "mistral"
DEFAULT_INDEX = str(
    Path(__file__).resolve().parents[1] / "indexes/e5_plus_0710/index.jsonl"
)
DEFAULT_E5_MODEL = "intfloat/multilingual-e5-base"

ABSTENTION_MESSAGE = (
    "Je n'ai pas trouvé d'information suffisamment fiable dans la documentation collectée."
)


def call_ollama(
    messages: list[dict[str, str]],
    model: str = DEFAULT_MODEL,
    url: str = DEFAULT_OLLAMA_URL,
    temperature: float = 0.1,
    top_p: float = 0.8,
    num_predict: int = 600,
    timeout: int = 180,
) -> str:
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature,
            "top_p": top_p,
            "num_predict": num_predict,
        },
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(
            "Cannot contact Ollama. Start it with `ollama serve` and make sure "
            f"the model `{model}` is installed."
        ) from exc

    message = body.get("message", {})
    content = message.get("content")
    if not content:
        raise RuntimeError(f"Unexpected Ollama response: {body}")
    return content.strip()


def source_report(hits: list[dict]) -> list[dict[str, Any]]:
    report = []
    for rank, hit in enumerate(hits, start=1):
        metadata = hit.get("metadata", {})
        report.append(
            {
                "rank": rank,
                "score": hit.get("score"),
                "semantic_score": hit.get("semantic_score"),
                "title": metadata.get("title"),
                "section_title": metadata.get("section_title"),
                "source_url": metadata.get("source_url"),
                "quality_status": metadata.get("quality_status"),
                "review_priority": metadata.get("review_priority"),
            }
        )
    return report


def answer_question(args: argparse.Namespace) -> dict[str, Any]:
    hits = retrieve(
        args.question,
        index_path=args.index,
        model_name=args.embedding_model,
        top_k=args.top_k,
        min_score=args.min_score,
        route_boost_weight=args.route_boost_weight,
    )

    if args.confidence_threshold is not None:
        abstain, reason = should_abstain(
            hits,
            min_top_score=args.confidence_threshold,
            min_semantic_score=args.semantic_threshold,
        )
        if abstain:
            return {
                "question": args.question,
                "model": args.model,
                "mode": "standard",
                "abstain": True,
                "abstention_reason": reason,
                "answer": ABSTENTION_MESSAGE,
                "sources": source_report(hits),
            }

    prompt = build_prompt(
        args.question,
        hits,
        mode="standard",
        max_context_chars=args.max_context_chars,
        max_chunk_chars=args.max_chunk_chars,
        include_scores=not args.hide_scores,
    )

    if args.dry_run:
        return {
            "question": args.question,
            "model": args.model,
            "mode": "standard",
            "abstain": False,
            "dry_run": True,
            "prompt": prompt.as_text_prompt(),
            "sources": source_report(hits),
        }

    response = call_ollama(
        prompt.as_messages(),
        model=args.model,
        url=args.ollama_url,
        temperature=args.temperature,
        top_p=args.top_p,
        num_predict=args.num_predict,
        timeout=args.timeout,
    )

    return {
        "question": args.question,
        "model": args.model,
        "mode": "standard",
        "abstain": False,
        "answer": response,
        "sources": source_report(hits),
    }


def print_text_result(result: dict[str, Any]) -> None:
    if result.get("dry_run"):
        print(result["prompt"])
        print("\n--- Retrieved sources ---")
    else:
        print(result["answer"])
        print("\n--- Retrieved sources ---")

    for source in result.get("sources", []):
        print(
            f"[{source['rank']}] score={source.get('score')} "
            f"semantic={source.get('semantic_score')} "
            f"{source.get('title') or 'Sans titre'} / "
            f"{source.get('section_title') or 'Sans section'}"
        )
        print(f"    {source.get('source_url')}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="RAG + Ministral 8B via Ollama + standard prompt."
    )
    parser.add_argument("question")
    parser.add_argument("--index", default=DEFAULT_INDEX)
    parser.add_argument("--embedding-model", default=DEFAULT_E5_MODEL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    parser.add_argument("--route-boost-weight", type=float, default=1.0)
    parser.add_argument("--max-context-chars", type=int, default=6000)
    parser.add_argument("--max-chunk-chars", type=int, default=1200)
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--top-p", type=float, default=0.8)
    parser.add_argument("--num-predict", type=int, default=600)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--confidence-threshold", type=float, default=None)
    parser.add_argument("--semantic-threshold", type=float, default=None)
    parser.add_argument("--hide-scores", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        result = answer_question(args)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text_result(result)


if __name__ == "__main__":
    main()
