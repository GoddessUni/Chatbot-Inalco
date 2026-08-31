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
    ("Emplois du temps", ("emploi du temps", "planning")),
    ("Numérique et outils", ("moodle", "messagerie", "compte numérique", "wifi", "eduroam", "webmail")),
    ("Bibliothèque", ("bibliothèque", "ressources documentaires", "bulac")),
    ("Examens", ("examen", "rattrapage", "partiel", "épreuve")),
    ("Inscriptions", ("inscription", "réinscription", "admission", "candidature")),
    ("Bourses et aides", ("bourse", "aide financière", "crous", "dossier social étudiant")),
    ("Logement", ("logement", "résidence universitaire")),
    ("Santé et bien-être", ("santé", "psychologue", "bien-être", "service de santé étudiant")),
    ("Orientation et insertion", ("orientation", "insertion", "stage", "alternance")),
    ("International", ("international", "erasmus", "mobilité")),
    ("Associations et vie de campus", ("association", "vie de campus", "engagement étudiant")),
)

URL_THEME_RULES = (
    ("/autres/emplois-du-temps", "Emplois du temps"),
    ("/services-et-ressources-numeriques", "Numérique et outils"),
    ("/candidatures-et-re-inscriptions/", "Inscriptions"),
    ("/foire-aux-questions-faq-procedure-dinscription", "Inscriptions"),
    ("/faq-admission-en-master", "Inscriptions"),
    ("/droits-de-scolarite-tarifs-exoneration-annulation-remboursement", "Inscriptions"),
    ("/scolarite-au-quotidien/", "Scolarité"),
    ("/harcelement-racisme-et-vss", "Harcèlement et VSS"),
    ("/mission-handicap", "Handicap"),
    ("/sante-sport-et-bien-etre/", "Santé et bien-être"),
    ("/insertion-professionnelle/", "Orientation et insertion"),
    ("/international/", "International"),
    ("/associations/", "Associations et vie de campus"),
)


def detect_risk_level(text: str) -> str:
    lower = text.lower()

    if any(keyword in lower for keyword in HIGH_RISK_KEYWORDS):
        return "high"

    if any(keyword in lower for keyword in MEDIUM_RISK_KEYWORDS):
        return "medium"

    return "low"


def detect_theme(
    text: str,
    title: str = "",
    section_title: str = "",
    source_url: str = "",
) -> str:
    lower_url = source_url.lower()
    for path, theme in URL_THEME_RULES:
        if path in lower_url:
            # Des titres plus spécifiques peuvent couvrir une large partie de catégories
            heading_text = f"{title}\n{section_title}".lower()
            for heading_theme, keywords in THEMES:
                if any(keyword in heading_text for keyword in keywords):
                    return heading_theme
            return theme

    heading_text = f"{title}\n{section_title}".lower()
    for theme, keywords in THEMES:
        if any(keyword in heading_text for keyword in keywords):
            return theme

    lower = text.lower()

    for theme, keywords in THEMES:
        if any(keyword in lower for keyword in keywords):
            return theme

    return "Général"


def enrich_chunk(chunk: dict) -> dict:
    chunk = dict(chunk)
    searchable_text = (
        f"{chunk.get('title', '')}\n"
        f"{chunk.get('section_title', '')}\n"
        f"{chunk['text']}"
    )
    chunk["risk_level"] = detect_risk_level(searchable_text)
    chunk["theme"] = detect_theme(
        chunk["text"],
        title=chunk.get("title", ""),
        section_title=chunk.get("section_title", ""),
        source_url=chunk.get("source_url", ""),
    )
    return chunk
