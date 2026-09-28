from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path


CATEGORY_RULES = (
    ("environnement", ("dd&rse", "durable", "environnement", "vélo", "eau", "vivier")),
    ("admission", ("candidater", "candidature", "admission", "parcoursup", "mon master")),
    ("inscriptions", ("inscription", "cvec", "droits d'inscription", "exonération")),
    ("examens", ("examen", "rattrapage", "ajac", "notes", "contrôle des connaissances")),
    ("aides", ("bourse", "aide financière", "aide alimentaire", "assistante sociale")),
    ("logement_restauration", ("logement", "restaurant", "cafétéria", "repas", "izly")),
    ("numerique", ("moodle", "numérique", "wi-fi", "compte", "électronique")),
    ("sante_securite", ("santé", "mal-être", "harcèlement", "violence", "urgence", "handicap")),
    ("international", ("international", "étranger", "erasmus", "mobilité", "réfugi")),
    ("orientation_insertion", ("orientation", "insertion", "stage", "alternance", "débouchés")),
    ("vie_etudiante", ("association", "engagement", "campus", "bibliothèque", "médiathèque")),
    ("formations", ("formation", "licence", "master", "langue", "parcours", "brochure", "cours")),
)

HIGH_RISK_TERMS = (
    "admission",
    "candidater",
    "inscription",
    "droits d'inscription",
    "exonération",
    "bourse",
    "examen",
    "rattrapage",
    "ajac",
    "handicap",
    "harcèlement",
    "violence",
    "urgence",
)


def load_questions(path: Path) -> list[str]:
    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def detect_category(question: str) -> str:
    lower = question.lower()
    for category, terms in CATEGORY_RULES:
        if any(term in lower for term in terms):
            return category
    return "general"


def detect_risk(question: str) -> str:
    lower = question.lower()
    if any(term in lower for term in HIGH_RISK_TERMS):
        return "high"
    if any(term in lower for term in ("adresse", "horaire", "contact", "où", "quand")):
        return "medium"
    return "low"


def retrieve_candidates(
    question: str,
    index: list[dict],
    encode_query,
    cosine,
    detect_routes,
    route_boost,
    rerank_bonus,
    top_k: int,
    model_name: str,
    route_boost_weight: float,
) -> list[dict]:
    query_vector = encode_query(question, model_name=model_name)
    routes = detect_routes(question)
    hits = []

    for record in index:
        semantic_score = cosine(query_vector, record["vector"])
        heuristic_score = route_boost(record, routes)
        heuristic_score += rerank_bonus(record, question, routes)
        score = semantic_score + route_boost_weight * heuristic_score
        metadata = record.get("metadata", {})
        hits.append(
            {
                "chunk_id": record.get("chunk_id"),
                "score": round(score, 4),
                "semantic_score": round(semantic_score, 4),
                "text": record.get("text", ""),
                "source_url": metadata.get("source_url"),
                "title": metadata.get("title"),
                "section_title": metadata.get("section_title"),
                "document_title": metadata.get("document_title"),
                "page_start": metadata.get("page_start"),
                "page_end": metadata.get("page_end"),
                "knowledge_type": metadata.get("knowledge_type"),
                "quality_status": metadata.get("quality_status"),
                "review_priority": metadata.get("review_priority"),
            }
        )

    return sorted(hits, key=lambda row: row["score"], reverse=True)[:top_k]


def write_jsonl(records: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_review_csv(records: list[dict], path: Path, top_k: int) -> None:
    base_fields = [
        "question_id",
        "question",
        "category",
        "risk_level",
        "split",
        "answerable_by_official_site",
        "answerable_by_kb",
        "requires_clarification",
        "expected_behavior",
        "gold_candidate_ranks",
        "manual_source_title",
        "manual_source_section",
        "manual_source_url",
        "manual_source_page",
        "gold_facts",
        "source_verified_at",
        "annotator",
        "notes",
    ]
    candidate_fields = []
    for rank in range(1, top_k + 1):
        candidate_fields.extend(
            [
                f"candidate_{rank}_title",
                f"candidate_{rank}_section",
                f"candidate_{rank}_url",
                f"candidate_{rank}_page",
                f"candidate_{rank}_score",
                f"candidate_{rank}_text",
            ]
        )

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=base_fields + candidate_fields)
        writer.writeheader()
        for record in records:
            clarify = "XXX" in record["question"]
            row = {
                "question_id": record["question_id"],
                "question": record["question"],
                "category": record["category"],
                "risk_level": record["risk_level"],
                "split": "unassigned",
                "answerable_by_official_site": "false" if clarify else "",
                "answerable_by_kb": "false" if clarify else "",
                "requires_clarification": "true" if clarify else "false",
                "expected_behavior": "clarify" if clarify else "",
                "gold_candidate_ranks": "",
                "manual_source_title": "",
                "manual_source_section": "",
                "manual_source_url": "",
                "manual_source_page": "",
                "gold_facts": "",
                "source_verified_at": "",
                "annotator": "",
                "notes": "",
            }
            for rank, candidate in enumerate(record["candidate_evidence"], start=1):
                start = candidate.get("page_start")
                end = candidate.get("page_end")
                page = ""
                if start is not None:
                    page = str(start) if end in (None, start) else f"{start}-{end}"
                row.update(
                    {
                        f"candidate_{rank}_title": candidate.get("document_title")
                        or candidate.get("title")
                        or "",
                        f"candidate_{rank}_section": candidate.get("section_title") or "",
                        f"candidate_{rank}_url": candidate.get("source_url") or "",
                        f"candidate_{rank}_page": page,
                        f"candidate_{rank}_score": candidate.get("score"),
                        f"candidate_{rank}_text": candidate.get("text") or "",
                    }
                )
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create an evidence-candidate dataset from Inalco questions."
    )
    parser.add_argument("--questions", required=True, type=Path)
    parser.add_argument("--index", required=True, type=Path)
    parser.add_argument("--project-root", default=Path.cwd(), type=Path)
    parser.add_argument("--output-jsonl", required=True, type=Path)
    parser.add_argument("--output-csv", required=True, type=Path)
    parser.add_argument("--model", default="intfloat/multilingual-e5-base")
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument("--route-boost-weight", type=float, default=1.0)
    args = parser.parse_args()

    rag_dir = args.project_root / "rag"
    sys.path.insert(0, str(rag_dir))
    from e5_embedder import cosine, encode_query
    from retrieve import detect_routes, rerank_bonus, route_boost

    questions = load_questions(args.questions)
    index = load_jsonl(args.index)
    records = []

    for number, question in enumerate(questions, start=1):
        print(f"[{number}/{len(questions)}] {question}")
        candidates = retrieve_candidates(
            question,
            index,
            encode_query,
            cosine,
            detect_routes,
            route_boost,
            rerank_bonus,
            args.top_k,
            args.model,
            args.route_boost_weight,
        )
        records.append(
            {
                "question_id": f"q{number:03d}",
                "question": question,
                "category": detect_category(question),
                "risk_level": detect_risk(question),
                "split": "unassigned",
                "answerable_by_official_site": None,
                "answerable_by_kb": None,
                "requires_clarification": "XXX" in question,
                "expected_behavior": "clarify" if "XXX" in question else None,
                "gold_facts": [],
                "gold_evidence": [],
                "verification_status": "pending_human_review",
                "candidate_evidence": candidates,
            }
        )

    write_jsonl(records, args.output_jsonl)
    write_review_csv(records, args.output_csv, args.top_k)
    print(f"Questions: {len(records)}")
    print(f"Candidate JSONL: {args.output_jsonl}")
    print(f"Review CSV: {args.output_csv}")


if __name__ == "__main__":
    main()
