HIGH_RISK_KEYWORDS = (
    "inscription",
    "réinscription",
    "admission",
    "droits de scolarité",
    "tarifs",
    "bourse",
    "logement",
    "examen",
    "rattrapage",
    "calendrier",
    "handicap",
    "santé",
    "psychologue",
    "harcèlement",
    "vss",
)

MEDIUM_RISK_KEYWORDS = (
    "contact",
    "mail",
    "email",
    "adresse",
    "horaire",
    "rendez-vous",
    "formulaire",
    "secrétariat",
)

THEMES = (
    ("Harcèlement et VSS", ("harcèlement", "vss", "violence sexiste", "violences sexuelles")),
    ("Handicap", ("handicap", "paeh", "mdph", "aménagement")),
    ("Examens", ("examen", "rattrapage", "partiel", "épreuve")),
    ("Emplois du temps", ("emploi du temps", "planning")),
    ("Inscriptions", ("inscription", "réinscription", "admission", "candidature")),
    ("Bibliothèque", ("bibliothèque", "ressources numériques", "bulac")),
    ("Bourses et aides", ("bourse", "aide financière", "crous", "dossier social étudiant")),
    ("Logement", ("logement", "résidence universitaire")),
    ("Santé et bien-être", ("santé", "psychologue", "bien-être", "service de santé étudiant")),
    ("Numérique et outils", ("moodle", "messagerie", "compte numérique", "wifi", "eduroam")),
    ("Orientation et insertion", ("orientation", "insertion", "stage", "alternance")),
    ("International", ("international", "erasmus", "mobilité")),
    ("Associations et vie de campus", ("association", "vie de campus", "engagement étudiant")),
)


def detect_risk_level(text: str) -> str:
    lower = text.lower()

    if any(keyword in lower for keyword in HIGH_RISK_KEYWORDS):
        return "high"

    if any(keyword in lower for keyword in MEDIUM_RISK_KEYWORDS):
        return "medium"

    return "low"


def detect_theme(text: str) -> str:
    lower = text.lower()

    for theme, keywords in THEMES:
        if any(keyword in lower for keyword in keywords):
            return theme

    return "Général"


def enrich_chunk(chunk: dict) -> dict:
    chunk = dict(chunk)
    searchable_text = f"{chunk.get('title', '')}\n{chunk['text']}"
    chunk["risk_level"] = detect_risk_level(searchable_text)
    chunk["theme"] = detect_theme(searchable_text)
    return chunk
