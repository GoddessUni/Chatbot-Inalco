from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from prompts import build_prompt, should_abstain
from retrieve_e5 import retrieve


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CURRENT_INDEX = PROJECT_ROOT / "indexes/current/index.jsonl"
LEGACY_INDEX = PROJECT_ROOT / "indexes/e5_plus_0710/index.jsonl"
DEFAULT_API_URL = os.getenv(
    "VLLM_API_URL", "http://127.0.0.1:8000/v1/chat/completions"
)
DEFAULT_MODEL = os.getenv(
    "VLLM_MODEL", "mistralai/Ministral-8B-Instruct-2410"
)
DEFAULT_INDEX = os.getenv(
    "RAG_INDEX_PATH", str(CURRENT_INDEX if CURRENT_INDEX.exists() else LEGACY_INDEX)
)
DEFAULT_E5_MODEL = os.getenv(
    "RAG_EMBEDDING_MODEL", "intfloat/multilingual-e5-base"
)

EXPERIMENT_METHODS = (
    "m0_llm_only",
    "m1_rag_simple",
    "m2_rag_rerank",
    "m3_rag_threshold",
    "m4_rag_abstention",
)

ABSTENTION_MESSAGE = (
    "Je n'ai pas trouve d'information suffisamment fiable dans la documentation "
    "collectee."
)


def resolve_method(args: argparse.Namespace) -> dict[str, Any]:
    method = getattr(args, "method", "m2_rag_rerank")
    if method not in EXPERIMENT_METHODS:
        allowed = ", ".join(EXPERIMENT_METHODS)
        raise RuntimeError(f"Unknown experiment method: {method}. Allowed: {allowed}")

    route_boost_weight = float(getattr(args, "route_boost_weight", 1.0))
    configs = {
        "m0_llm_only": {
            "use_retrieval": False,
            "retrieval_mode": "none",
            "route_boost_weight": 0.0,
            "prompt_mode": "llm_only",
            "use_threshold": False,
        },
        "m1_rag_simple": {
            "use_retrieval": True,
            "retrieval_mode": "semantic",
            "route_boost_weight": 0.0,
            "prompt_mode": "standard",
            "use_threshold": False,
        },
        "m2_rag_rerank": {
            "use_retrieval": True,
            "retrieval_mode": "heuristic_rerank",
            "route_boost_weight": route_boost_weight,
            "prompt_mode": "standard",
            "use_threshold": False,
        },
        "m3_rag_threshold": {
            "use_retrieval": True,
            "retrieval_mode": "semantic",
            "route_boost_weight": 0.0,
            "prompt_mode": "standard",
            "use_threshold": True,
        },
        "m4_rag_abstention": {
            "use_retrieval": True,
            "retrieval_mode": "semantic",
            "route_boost_weight": 0.0,
            "prompt_mode": "strict_abstention",
            "use_threshold": False,
        },
    }
    config = dict(configs[method])
    config["method"] = method

    if config["use_threshold"]:
        confidence = getattr(args, "confidence_threshold", None)
        semantic = getattr(args, "semantic_threshold", None)
        if confidence is None and semantic is None:
            raise RuntimeError(
                "m3_rag_threshold requires --confidence-threshold and/or "
                "--semantic-threshold calibrated on the validation set."
            )

    return config


def call_vllm(
    messages: list[dict[str, str]],
    model: str = DEFAULT_MODEL,
    url: str = DEFAULT_API_URL,
    temperature: float = 0.1,
    top_p: float = 0.8,
    max_tokens: int = 600,
    seed: int = 42,
    timeout: int = 600,
) -> str:
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens,
        "seed": seed,
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"vLLM returned HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(
            "Cannot contact vLLM. Check that the server is running on "
            f"{url} and that the SSH tunnel is active when calling it remotely."
        ) from exc

    choices = body.get("choices") or []
    if not choices:
        raise RuntimeError(f"Unexpected vLLM response: {body}")
    content = (choices[0].get("message") or {}).get("content")
    if not content:
        raise RuntimeError(f"vLLM returned an empty answer: {body}")
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
                "audience": metadata.get("audience", ["all"]),
                "journey_stage": metadata.get("journey_stage", "general"),
                "academic_years": metadata.get("academic_years", []),
                "source_url": metadata.get("source_url"),
                "parent_url": metadata.get("parent_url"),
                "document_title": metadata.get("document_title"),
                "page_start": metadata.get("page_start"),
                "page_end": metadata.get("page_end"),
                "validity_period": metadata.get("validity_period"),
                "quality_status": metadata.get("quality_status"),
                "review_priority": metadata.get("review_priority"),
            }
        )
    return report


def answer_question(args: argparse.Namespace) -> dict[str, Any]:
    config = resolve_method(args)
    hits = []
    if config["use_retrieval"]:
        hits = retrieve(
            args.question,
            index_path=args.index,
            model_name=args.embedding_model,
            top_k=args.top_k,
            min_score=args.min_score,
            route_boost_weight=config["route_boost_weight"],
        )

    if config["use_threshold"]:
        min_top_score = (
            args.confidence_threshold
            if args.confidence_threshold is not None
            else float("-inf")
        )
        abstain, reason = should_abstain(
            hits,
            min_top_score=min_top_score,
            min_semantic_score=args.semantic_threshold,
        )
        if abstain:
            return {
                "question": args.question,
                "model": args.model,
                "backend": "vllm",
                "method": config["method"],
                "experiment_id": getattr(args, "experiment_id", None) or config["method"],
                "mode": config["prompt_mode"],
                "prompt_mode": config["prompt_mode"],
                "retrieval_mode": config["retrieval_mode"],
                "route_boost_weight": config["route_boost_weight"],
                "confidence_threshold": args.confidence_threshold,
                "semantic_threshold": args.semantic_threshold,
                "abstain": True,
                "abstention_reason": reason,
                "answer": ABSTENTION_MESSAGE,
                "sources": source_report(hits),
            }

    prompt = build_prompt(
        args.question,
        hits,
        mode=config["prompt_mode"],
        max_context_chars=args.max_context_chars,
        max_chunk_chars=args.max_chunk_chars,
        include_scores=not args.hide_scores,
    )

    if args.dry_run:
        return {
            "question": args.question,
            "model": args.model,
            "backend": "vllm",
            "method": config["method"],
            "experiment_id": getattr(args, "experiment_id", None) or config["method"],
            "mode": config["prompt_mode"],
            "prompt_mode": config["prompt_mode"],
            "retrieval_mode": config["retrieval_mode"],
            "route_boost_weight": config["route_boost_weight"],
            "confidence_threshold": getattr(args, "confidence_threshold", None),
            "semantic_threshold": getattr(args, "semantic_threshold", None),
            "abstain": False,
            "dry_run": True,
            "prompt": prompt.as_text_prompt(),
            "sources": source_report(hits),
        }

    response = call_vllm(
        prompt.as_messages(),
        model=args.model,
        url=args.api_url,
        temperature=args.temperature,
        top_p=args.top_p,
        max_tokens=args.num_predict,
        seed=args.seed,
        timeout=args.timeout,
    )

    return {
        "question": args.question,
        "model": args.model,
        "backend": "vllm",
        "method": config["method"],
        "experiment_id": getattr(args, "experiment_id", None) or config["method"],
        "mode": config["prompt_mode"],
        "prompt_mode": config["prompt_mode"],
        "retrieval_mode": config["retrieval_mode"],
        "route_boost_weight": config["route_boost_weight"],
        "confidence_threshold": getattr(args, "confidence_threshold", None),
        "semantic_threshold": getattr(args, "semantic_threshold", None),
        "abstain": False,
        "answer": response,
        "sources": source_report(hits),
    }


def print_text_result(result: dict[str, Any]) -> None:
    print(result.get("prompt") if result.get("dry_run") else result["answer"])
    print("\n--- Retrieved sources ---")
    for source in result.get("sources", []):
        print(
            f"[{source['rank']}] score={source.get('score')} "
            f"semantic={source.get('semantic_score')} "
            f"{source.get('title') or 'Sans titre'} / "
            f"{source.get('section_title') or 'Sans section'}"
        )
        if source.get("page_start") is not None:
            page_end = source.get("page_end") or source["page_start"]
            page_label = (
                str(source["page_start"])
                if page_end == source["page_start"]
                else f"{source['page_start']}-{page_end}"
            )
            print(f"    PDF page(s): {page_label}")
        print(f"    {source.get('source_url')}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inalco RAG + Ministral 8B served by vLLM."
    )
    parser.add_argument("question")
    parser.add_argument(
        "--method",
        choices=EXPERIMENT_METHODS,
        default="m2_rag_rerank",
        help="Controlled experiment condition (default preserves current behavior).",
    )
    parser.add_argument("--experiment-id", default=None)
    parser.add_argument("--index", default=DEFAULT_INDEX)
    parser.add_argument("--embedding-model", default=DEFAULT_E5_MODEL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--api-url", default=DEFAULT_API_URL)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    parser.add_argument("--route-boost-weight", type=float, default=1.0)
    parser.add_argument("--max-context-chars", type=int, default=6000)
    parser.add_argument("--max-chunk-chars", type=int, default=1200)
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--top-p", type=float, default=0.8)
    parser.add_argument("--num-predict", type=int, default=600)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--timeout", type=int, default=600)
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
