import argparse
import json
from pathlib import Path

from e5_embedder import DEFAULT_E5_MODEL, cosine, encode_query
from retrieve import (
    detect_routes,
    rerank_bonus,
    route_boost,
    select_intent_candidates,
)


def load_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def retrieve(
    question: str,
    index_path: str | Path,
    model_name: str = DEFAULT_E5_MODEL,
    top_k: int = 5,
    min_score: float = 0.0,
    route_boost_weight: float = 1.0,
) -> list[dict]:
    index = load_jsonl(index_path)
    query_vector = encode_query(question, model_name=model_name)
    routes = detect_routes(question)

    hits = []
    for record in select_intent_candidates(index, question):
        semantic_score = cosine(query_vector, record["vector"])
        score = semantic_score
        heuristic_score = route_boost(record, routes)
        heuristic_score += rerank_bonus(record, question, routes)
        score += route_boost_weight * heuristic_score
        if score >= min_score:
            hit = dict(record)
            hit["semantic_score"] = round(semantic_score, 4)
            hit["score"] = round(score, 4)
            hit["routes"] = routes
            hits.append(hit)

    return sorted(hits, key=lambda item: item["score"], reverse=True)[:top_k]


def print_hits(hits: list[dict]) -> None:
    for rank, hit in enumerate(hits, start=1):
        metadata = hit["metadata"]
        print(f"\n[{rank}] score={hit['score']}")
        if "semantic_score" in hit:
            print(f"semantic_score: {hit['semantic_score']}")
        print(f"title: {metadata.get('title')}")
        print(f"section: {metadata.get('section_title')}")
        print(f"theme: {metadata.get('theme')}")
        print(f"quality: {metadata.get('quality_status')} / {metadata.get('review_priority')}")
        print(f"source: {metadata.get('source_url')}")
        text = (hit.get("text") or "").replace("\n", " ")
        print(f"text: {text[:700]}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--index", default="indexes/e5_base/index.jsonl")
    parser.add_argument("--model", default=DEFAULT_E5_MODEL)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    parser.add_argument("--route-boost-weight", type=float, default=1.0)
    args = parser.parse_args()
    print_hits(
        retrieve(
            args.question,
            args.index,
            model_name=args.model,
            top_k=args.top_k,
            min_score=args.min_score,
            route_boost_weight=args.route_boost_weight,
        )
    )


if __name__ == "__main__":
    main()
