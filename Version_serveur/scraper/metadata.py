import re


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
    (
        "Environnement et responsabilité sociale",
        (
            "dd&rse",
            "développement durable",
            "responsabilité sociale",
            "responsabilité sociétale",
            "transition écologique",
            "impact environnemental",
        ),
    ),
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
    ("/ddrse", "Environnement et responsabilité sociale"),
    ("/associations/", "Associations et vie de campus"),
)

PROSPECTIVE_PATH_PARTS = (
    "/candidatures",
    "/candidater-",
    "/faq-admission-",
)

FORMATION_PATH_PARTS = (
    "/nos-formations",
    "/formations-",
    "/formations/",
    "-brochures",
)

ADMINISTRATIVE_ENROLLMENT_PATH_PARTS = (
    "inscription-et-reinscription-administrative",
    "inscriptions-administratives",
    "procedure-dinscription",
    "droits-de-scolarite",
)

ACADEMIC_ENROLLMENT_PATH_PARTS = (
    "inscriptions-pedagogiques",
    "inscription-et-reinscription-pedagogique",
)

ENROLLED_STUDENT_PATH_PARTS = (
    "/examens",
    "/scolarite-au-quotidien/",
    "/autres/emplois-du-temps",
    "/schema-directeur-de-la-vie-etudiante",
)

ACADEMIC_YEAR_PATTERN = re.compile(r"\b20\d{2}\s*[-–/]\s*20\d{2}\b")


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


def detect_audience(source_url: str) -> list[str]:
    lower_url = source_url.lower()

    if any(part in lower_url for part in PROSPECTIVE_PATH_PARTS):
        return ["prospective_student"]

    if any(part in lower_url for part in ADMINISTRATIVE_ENROLLMENT_PATH_PARTS):
        return ["prospective_student", "admitted_not_enrolled", "enrolled_student"]

    if any(part in lower_url for part in FORMATION_PATH_PARTS):
        return ["prospective_student", "enrolled_student"]

    if any(part in lower_url for part in ACADEMIC_ENROLLMENT_PATH_PARTS):
        return ["enrolled_student"]

    if any(part in lower_url for part in ENROLLED_STUDENT_PATH_PARTS):
        return ["enrolled_student"]

    return ["all"]


def detect_journey_stage(source_url: str) -> str:
    lower_url = source_url.lower()

    if any(part in lower_url for part in PROSPECTIVE_PATH_PARTS):
        return "application"
    if any(part in lower_url for part in ADMINISTRATIVE_ENROLLMENT_PATH_PARTS):
        return "administrative_enrollment"
    if any(part in lower_url for part in ACADEMIC_ENROLLMENT_PATH_PARTS):
        return "academic_enrollment"
    if any(part in lower_url for part in FORMATION_PATH_PARTS):
        return "programme_selection"
    if any(part in lower_url for part in ENROLLED_STUDENT_PATH_PARTS):
        return "studies"
    return "general"


def detect_academic_years(text: str) -> list[str]:
    years = {
        re.sub(r"\s*[-–/]\s*", "-", match)
        for match in ACADEMIC_YEAR_PATTERN.findall(text)
    }
    return sorted(years)


def enrich_chunk(chunk: dict) -> dict:
    chunk = dict(chunk)
    source_hint = "\n".join(
        value
        for value in (chunk.get("source_url", ""), chunk.get("parent_url", ""))
        if value
    )
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
        source_url=source_hint,
    )
    chunk["audience"] = detect_audience(source_hint)
    chunk["journey_stage"] = detect_journey_stage(source_hint)
    chunk["academic_years"] = detect_academic_years(searchable_text)
    return chunk
