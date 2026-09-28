import argparse
import json
import re
import unicodedata
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

ACCESS_STRONG_TRIGGERS = (
    "se rendre",
    "transport",
    "transports",
    "métro",
    "metro",
    "rer",
    "tramway",
    "bus",
)

ACCESS_ATTRIBUTE_TRIGGERS = (
    "adresse",
    "adresses",
    "horaire",
    "horaires",
    "ouverture",
    "fermeture",
    "ouvert",
    "ouverte",
    "où se trouve",
    "ou se trouve",
    "site",
    "sites",
)

INCOMING_MOBILITY_URL_PARTS = (
    "/international/venir-etudier-a-l-inalco",
)

OUTGOING_MOBILITY_URL_PARTS = (
    "/international/etudier-a-l-etranger/",
)

LANGUAGE_CATALOGUE_URL_PARTS = (
    "/les-langues-et-civilisations-enseignees-linalco",
)

INCOMING_MOBILITY_TRIGGERS = (
    "venir etudier a l'inalco",
    "venir etudier a inalco",
    "etudier a l'inalco dans le cadre d'un programme d'echange",
    "etudier a inalco dans le cadre d'un programme d'echange",
    "mobilite entrante",
)

OUTGOING_MOBILITY_TRIGGERS = (
    "etudier a l'etranger",
    "partir a l'etranger",
    "partir en mobilite",
    "mobilite sortante",
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
            "transport",
            "transports",
            "métro",
            "metro",
            "rer",
            "tramway",
            "bus",
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
    "admission": {
        "triggers": (
            "admission",
            "admissions",
            "candidature",
            "candidatures",
            "candidater",
            "postuler",
            "parcoursup",
            "mon master",
            "ecandidat",
            "études en france",
            "etudes en france",
            "pièce justificative",
            "pièces justificatives",
            "inscription administrative",
            "inscriptions administratives",
        ),
        "expansion": (
            "admission candidature candidater conditions calendrier pièces justificatives "
            "Parcoursup Mon Master eCandidat Études en France inscription administrative"
        ),
        "boost_terms": (
            "admission",
            "candidature",
            "candidater",
            "parcoursup",
            "mon master",
            "ecandidat",
            "études en france",
            "etudes en france",
            "inscription administrative",
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
            "parking a velo",
            "garage à vélo",
            "garage a velo",
            "fontaine",
            "distributeur d'eau",
            "distributeurs d'eau",
            "eau",
            "boîte à livres",
            "boite a livres",
            "boîte à don",
            "boîte à dons",
            "boite à don",
            "boite a don",
            "étagère à plante",
            "étagère à plantes",
            "etagere a plante",
            "etagere a plantes",
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


def normalize_search_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    normalized = "".join(
        char for char in normalized if not unicodedata.combining(char)
    )
    normalized = normalized.replace("’", "'").replace("‘", "'")
    return " ".join(normalized.casefold().split())


def mobility_direction(question: str) -> str | None:
    normalized = normalize_search_text(question)
    if any(trigger in normalized for trigger in INCOMING_MOBILITY_TRIGGERS):
        return "incoming"
    if any(trigger in normalized for trigger in OUTGOING_MOBILITY_TRIGGERS):
        return "outgoing"
    return None


def asks_language_catalogue(question: str) -> bool:
    normalized = normalize_search_text(question)
    if any(term in normalized for term in ("echange", "erasmus", "mobilite")):
        return False
    return any(
        phrase in normalized
        for phrase in (
            "quelles langues",
            "liste des langues",
            "langues enseignees",
            "langues proposees",
            "langues peut-on etudier",
            "langues puis-je etudier",
        )
    )


def directionally_compatible(record: dict, question: str) -> bool:
    direction = mobility_direction(question)
    if direction is None:
        return True

    metadata = record.get("metadata", {}) or {}
    source_url = str(metadata.get("source_url") or "").casefold()
    if direction == "incoming":
        return not any(part in source_url for part in OUTGOING_MOBILITY_URL_PARTS)
    return not any(part in source_url for part in INCOMING_MOBILITY_URL_PARTS)


def select_intent_candidates(records: list[dict], question: str) -> list[dict]:
    if asks_language_catalogue(question):
        catalogue = [
            record
            for record in records
            if any(
                part in str((record.get("metadata") or {}).get("source_url") or "").casefold()
                for part in LANGUAGE_CATALOGUE_URL_PARTS
            )
        ]
        if catalogue:
            return catalogue

    direction = mobility_direction(question)
    if direction is not None:
        preferred_parts = (
            INCOMING_MOBILITY_URL_PARTS
            if direction == "incoming"
            else OUTGOING_MOBILITY_URL_PARTS
        )
        preferred = [
            record
            for record in records
            if any(
                part in str((record.get("metadata") or {}).get("source_url") or "").casefold()
                for part in preferred_parts
            )
        ]
        if preferred:
            return preferred

    return [
        record for record in records if directionally_compatible(record, question)
    ]


def detect_routes(question: str) -> list[str]:
    normalized = question.casefold()
    routes = [
        route
        for route, config in ROUTES.items()
        if any(
            contains_trigger(normalized, trigger.casefold())
            for trigger in config["triggers"]
        )
    ]

    # Address, opening-hour and location words describe many student services.
    # They should not turn a restaurant or campus-service question into a query
    # about travelling to the Inalco buildings.
    topical_routes = [route for route in routes if route != "access"]
    if "access" in routes and topical_routes:
        has_strong_access_intent = any(
            contains_trigger(normalized, trigger)
            for trigger in ACCESS_STRONG_TRIGGERS
        )
        access_is_only_an_attribute = any(
            contains_trigger(normalized, trigger)
            for trigger in ACCESS_ATTRIBUTE_TRIGGERS
        )
        if access_is_only_an_attribute and not has_strong_access_intent:
            routes.remove("access")

    return routes


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
            metadata.get("audience"),
            metadata.get("journey_stage"),
            metadata.get("academic_years"),
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

    # Keep heuristic scores secondary to semantic similarity. Unbounded sums
    # made route-heavy scores incomparable with ordinary retrieval scores.
    return max(-0.45, min(bonus, 0.45))


def rerank_bonus(record: dict, question: str, routes: list[str]) -> float:
    bonus = 0.0
    # The large access bonus is reserved for a pure building-access query. On a
    # multi-topic query it would otherwise drown out the topical evidence.
    if routes == ["access"]:
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
    for record in select_intent_candidates(index, question):
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
