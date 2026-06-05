HIGH_RISK_KEYWORDS = [
    "inscription", "réinscription", "admission",
    "droits de scolarité", "tarifs", "bourse",
    "logement", "examen", "rattrapage",
    "calendrier", "handicap", "santé",
    "psychologue", "harcèlement", "vss"
]

MEDIUM_RISK_KEYWORDS = [
    "contact", "mail", "email", "adresse",
    "horaire", "rendez-vous", "formulaire"
]


def detect_risk_level(text: str) -> str:
    lower = text.lower()

    if any(k in lower for k in HIGH_RISK_KEYWORDS):
        return "high"

    if any(k in lower for k in MEDIUM_RISK_KEYWORDS):
        return "medium"

    return "low"


def detect_theme(text: str) -> str:
    lower = text.lower()

    if "moodle" in lower or "numérique" in lower or "messagerie" in lower:
        return "Numérique et outils"

    if "inscription" in lower or "scolarité" in lower or "examen" in lower:
        return "Scolarité"

    if "bourse" in lower or "logement" in lower:
        return "Aides et accompagnements"

    if "santé" in lower or "psychologue" in lower or "bien-être" in lower:
        return "Santé et bien-être"

    if "stage" in lower or "insertion professionnelle" in lower:
        return "Insertion professionnelle"

    return "Général"


def enrich_chunk(chunk: dict) -> dict:
    chunk["risk_level"] = detect_risk_level(chunk["text"])
    chunk["theme"] = detect_theme(chunk["text"])
    chunk["source_verified"] = True
    return chunk