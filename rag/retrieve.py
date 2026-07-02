import argparse
import json
from pathlib import Path

from hash_embedder import cosine, embed_text


ROUTES = {
    "restauration": {
        "triggers": (
            "manger",
            "nourrir",
            "restauration",
            "restaurant",
            "repas",
            "cantine",
            "cafeteria",
            "cafétéria",
            "izly",
        ),
        "expansion": "se nourrir restauration restaurant universitaire cafeteria cafetéria repas crous izly",
        "boost_terms": ("se nourrir", "restaurants", "cafétérias", "cafeterias", "repas", "izly"),
    },
    "logement": {
        "triggers": (
            "logement",
            "loger",
            "loyer",
            "residence",
            "résidence",
            "caf",
            "apl",
            "als",
            "alf",
        ),
        "expansion": "se loger logement residence résidence crous caf apl als alf loyer aides locatives",
        "boost_terms": ("se loger", "logement", "aides locatives", "caf", "apl", "résidence"),
    },
    "bourses": {
        "triggers": (
            "bourse",
            "bourses",
            "boursier",
            "boursiers",
            "dse",
            "aide sociale",
            "aides sociales",
            "crous",
        ),
        "expansion": "bourses aides sociales crous dossier social etudiant dse boursier aide financiere",
        "boost_terms": ("bourses", "aides sociales", "dossier social", "dse", "crous"),
    },
}


def load_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def detect_routes(question: str) -> list[str]:
    normalized = question.lower()
    return [
        route
        for route, config in ROUTES.items()
        if any(trigger in normalized for trigger in config["triggers"])
    ]


def expand_question(question: str, routes: list[str]) -> str:
    additions = [ROUTES[route]["expansion"] for route in routes]
    return " ".join([question, *additions])


def route_boost(record: dict, routes: list[str]) -> float:
    if not routes:
        return 0.0

    metadata = record.get("metadata", {})
    searchable = " ".join(
        str(value or "")
        for value in (
            metadata.get("title"),
            metadata.get("section_title"),
            metadata.get("theme"),
            metadata.get("source_url"),
            record.get("text"),
        )
    ).lower()

    boost = 0.0
    for route in routes:
        if any(term in searchable for term in ROUTES[route]["boost_terms"]):
            boost += 0.18
    return boost


def retrieve(
    question: str,
    index_path: str | Path,
    top_k: int = 5,
    min_score: float = 0.0,
) -> list[dict]:
    index = load_jsonl(index_path)
    dim = len(index[0]["vector"]) if index else 768
    routes = detect_routes(question)
    query_vector = embed_text(expand_question(question, routes), dim=dim)

    hits = []
    for record in index:
        score = cosine(query_vector, record["vector"]) + route_boost(record, routes)
        if score >= min_score:
            hit = dict(record)
            hit["score"] = round(score, 4)
            hit["routes"] = routes
            hits.append(hit)

    return sorted(hits, key=lambda item: item["score"], reverse=True)[:top_k]


def print_hits(hits: list[dict]) -> None:
    for rank, hit in enumerate(hits, start=1):
        metadata = hit["metadata"]
        print(f"\n[{rank}] score={hit['score']}")
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
    parser.add_argument("--index", default="indexes/prototype_hash/index.jsonl")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    args = parser.parse_args()
    print_hits(retrieve(args.question, args.index, args.top_k, args.min_score))


if __name__ == "__main__":
    main()
