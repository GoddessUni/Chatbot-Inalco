import argparse
import json
import re
from pathlib import Path

from hash_embedder import cosine, embed_text


ACCESS_AUTHORITATIVE_URL_PARTS = (
    "se-rendre-a-l-inalco",
    "le-pole-des-langues-et-civilisations",
    "la-maison-de-la-recherche",
)

ACCESS_MODE_TERMS = (
    "en métro",
    "en metro",
    "en rer",
    "en bus",
    "en tramway",
    "station",
    "arrêt",
    "arret",
    "ligne",
)

ACCESS_GENERIC_NOISE_TERMS = (
    "evento",
    "renater",
    "compte numérique",
    "services et ressources numériques",
    "carte multi-services",
)


ROUTES = {
    "restauration": {
        "triggers": (
            "manger",
            "nourrir",
            "restauration",
            "restaurant",
            "restaurants",
            "repas",
            "cantine",
            "cantines",
            "cafeteria",
            "cafeterias",
            "cafétéria",
            "cafétérias",
            "izly",
        ),
        "expansion": "se nourrir restauration restaurant universitaire cafeteria cafetéria repas crous izly",
        "boost_terms": (
            "se nourrir",
            "restaurant",
            "restaurants",
            "cafeteria",
            "cafeterias",
            "cafétéria",
            "cafétérias",
            "repas",
            "izly",
        ),
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
            "aide financière",
            "aides financières",
            "aide financiere",
            "aides financieres",
        ),
        "expansion": "bourses aides sociales crous dossier social etudiant dse boursier aide financiere",
        "boost_terms": ("bourses", "aides sociales", "dossier social", "dse", "crous"),
    },
    "access": {
        "triggers": (
            "adresse",
            "adresses",
            "horaire",
            "horaires",
            "ouverture",
            "fermeture",
            "ouvert",
            "ouverte",
            "accès",
            "acces",
            "se rendre",
            "venir",
            "aller",
            "où se trouve",
            "ou se trouve",
            "site",
            "sites",
            "plc",
            "maison de la recherche",
        ),
        "expansion": (
            "se rendre à l'Inalco adresse horaires ouverture accès sites "
            "Pôle des langues et civilisations PLC 65 rue des Grands Moulins "
            "Maison de la recherche 2 rue de Lille"
        ),
        "boost_terms": (
            "se rendre à l'inalco",
            "se rendre a l'inalco",
            "pôle des langues",
            "pole des langues",
            "65 rue des grands moulins",
            "maison de la recherche",
            "2 rue de lille",
            "horaires d'ouverture",
            "adresse",
        ),
    },
    "formation": {
        "triggers": (
            "formation",
            "formations",
            "licence",
            "master",
            "llcer",
            "brochure",
            "bilangue",
            "parcours",
            "professionnalisant",
            "tal",
            "traduction",
            "admission",
            "candidature",
        ),
        "expansion": (
            "formations licence master LLCER brochures parcours bilangue "
            "parcours professionnalisant TAL traduction spécialisée admission candidature"
        ),
        "boost_terms": (
            "formations",
            "licence llcer",
            "master",
            "brochures",
            "parcours bilangue",
            "parcours professionnalisant",
            "traduction spécialisée",
            "traitement automatique des langues",
        ),
    },
    "scolarite": {
        "triggers": (
            "inscription pédagogique",
            "inscriptions pédagogiques",
            "inscription pedagogique",
            "examens",
            "examen",
            "rattrapage",
            "rattrapages",
            "notes",
            "résultats",
            "resultats",
            "annales",
            "matière",
            "matiere",
            "option",
        ),
        "expansion": (
            "scolarité inscriptions pédagogiques examens rattrapages notes résultats "
            "annales options matières emploi du temps"
        ),
        "boost_terms": (
            "inscriptions pédagogiques",
            "inscriptions pedagogiques",
            "examens",
            "rattrapages",
            "notes",
            "résultats",
            "annales",
            "emploi du temps",
        ),
    },
    "campus_environment": {
        "triggers": (
            "vivier",
            "environnement",
            "développement durable",
            "developpement durable",
            "rse",
            "vélo",
            "velo",
            "parking vélo",
            "fontaine",
            "eau",
            "boîte à livres",
            "boite a livres",
            "graines",
            "plantes",
        ),
        "expansion": (
            "Vivier environnemental développement durable RSE campus parking vélo "
            "fontaine à eau boîte à livres graines plantes engagement écologique"
        ),
        "boost_terms": (
            "vivier",
            "développement durable",
            "developpement durable",
            "rse",
            "parking vélo",
            "parking velo",
            "fontaine à eau",
            "boîte à livres",
            "boite a livres",
        ),
    },
}


def load_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def contains_trigger(text: str, trigger: str) -> bool:
    pattern = rf"(?<!\w){re.escape(trigger)}(?!\w)"
    return re.search(pattern, text) is not None


def detect_routes(question: str) -> list[str]:
    normalized = question.casefold()
    return [
        route
        for route, config in ROUTES.items()
        if any(
            contains_trigger(normalized, trigger.casefold())
            for trigger in config["triggers"]
        )
    ]


def expand_question(question: str, routes: list[str]) -> str:
    additions = [ROUTES[route]["expansion"] for route in routes]
    return " ".join([question, *additions])


def route_boost(record: dict, routes: list[str]) -> float:
    if not routes:
        return 0.0

    metadata = record.get("metadata", {})
    metadata_searchable = " ".join(
        str(value or "")
        for value in (
            metadata.get("title"),
            metadata.get("section_title"),
            metadata.get("theme"),
            metadata.get("source_url"),
        )
    ).lower()
    content_searchable = str(record.get("text") or "").lower()

    boost = 0.0
    for route in routes:
        terms = ROUTES[route]["boost_terms"]
        if any(term in metadata_searchable for term in terms):
            boost += 0.18
        elif any(term in content_searchable for term in terms):
            boost += 0.06
    return boost


def access_rerank_bonus(record: dict, question: str) -> float:
    metadata = record.get("metadata", {})
    source_url = (metadata.get("source_url") or "").lower()
    title = (metadata.get("title") or "").lower()
    section = (metadata.get("section_title") or "").lower()
    text = (record.get("text") or "").lower()
    searchable = " ".join([source_url, title, section, text])
    normalized_question = question.lower()

    bonus = 0.0

    if any(part in source_url for part in ACCESS_AUTHORITATIVE_URL_PARTS):
        bonus += 0.28
    if "se rendre" in title or "accès" in section or "acces" in section:
        bonus += 0.18
    if any(site in searchable for site in ("pôle des langues", "pole des langues", "maison de la recherche")):
        bonus += 0.16
    if any(term in searchable for term in ACCESS_MODE_TERMS):
        bonus += 0.24

    asks_transport = any(
        term in normalized_question
        for term in ("se rendre", "venir", "aller", "accès", "acces", "transport")
    )
    if asks_transport and any(term in searchable for term in ACCESS_MODE_TERMS):
        bonus += 0.22

    asks_hours_or_address = any(
        term in normalized_question
        for term in ("adresse", "horaires", "horaire", "ouverture", "ouvert")
    )
    if asks_hours_or_address and any(
        term in searchable for term in ("adresse", "horaires", "horaire", "rue")
    ):
        bonus += 0.2

    if any(term in searchable for term in ACCESS_GENERIC_NOISE_TERMS):
        bonus -= 0.35
    if "services et ressources numériques" in title:
        bonus -= 0.4
    if "footer" in source_url:
        bonus -= 0.15

    return bonus


def rerank_bonus(record: dict, question: str, routes: list[str]) -> float:
    bonus = 0.0
    if "access" in routes:
        bonus += access_rerank_bonus(record, question)
    return bonus


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
        semantic_score = cosine(query_vector, record["vector"])
        score = semantic_score + route_boost(record, routes)
        score += rerank_bonus(record, question, routes)
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
