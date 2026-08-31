import argparse
import json
from pathlib import Path

from prompts import build_prompt, should_abstain
from retrieve_e5 import retrieve


ABSTENTION_MESSAGE = (
    "Je n'ai pas trouvé d'information suffisamment fiable dans la documentation collectée."
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--index", default="indexes/e5_plus/index.jsonl")
    parser.add_argument("--model", default="intfloat/multilingual-e5-base")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    parser.add_argument("--mode", choices=("standard", "strict_abstention"), default="standard")
    parser.add_argument("--max-context-chars", type=int, default=6000)
    parser.add_argument("--max-chunk-chars", type=int, default=1200)
    parser.add_argument("--confidence-threshold", type=float, default=None)
    parser.add_argument("--semantic-threshold", type=float, default=None)
    parser.add_argument("--json", action="store_true", help="Output messages as JSON.")
    args = parser.parse_args()

    hits = retrieve(
        args.question,
        index_path=args.index,
        model_name=args.model,
        top_k=args.top_k,
        min_score=args.min_score,
    )

    if args.confidence_threshold is not None:
        abstain, reason = should_abstain(
            hits,
            min_top_score=args.confidence_threshold,
            min_semantic_score=args.semantic_threshold,
        )
        if abstain:
            result = {
                "abstain": True,
                "reason": reason,
                "answer": ABSTENTION_MESSAGE,
                "hits": hits,
            }
            print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else ABSTENTION_MESSAGE)
            return

    prompt = build_prompt(
        args.question,
        hits,
        mode=args.mode,
        max_context_chars=args.max_context_chars,
        max_chunk_chars=args.max_chunk_chars,
    )

    if args.json:
        print(
            json.dumps(
                {
                    "abstain": False,
                    "messages": prompt.as_messages(),
                    "source_urls": prompt.source_urls,
                    "hits": hits,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print(prompt.as_text_prompt())


if __name__ == "__main__":
    main()
