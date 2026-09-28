PORTAIL_BASE_URL = "https://portail-etudiant.inalco.fr/fr/index.html"
PORTAIL_SITE_MAP_URL = (
    "https://portail-etudiant.inalco.fr/fr/footer/autres-liens/plan-du-site.html"
)

INALCO_CORE_PATHS = (
    "/candidatures",
    "/candidater-un-cursus-diplomant",
    "/nos-formations",
    "/les-langues-et-civilisations-enseignees-linalco",
    "/formations-diplomantes",
    "/formations/diplomes-detablissement",
    "/diplomes-detablissement-brochures",
    "/foire-aux-questions-faq-procedure-dinscription",
    "/inscriptions-administratives",
    "/faq-admission-en-master",
    "/droits-de-scolarite-tarifs-exoneration-annulation-remboursement",
    "/le-pole-des-langues-et-civilisations",
    "/la-maison-de-la-recherche",
    "/examens",
    "/inscriptions-pedagogiques",
    "/reglements-et-chartes-etudiantes",
    "/schema-directeur-de-la-vie-etudiante",
    "/ddrse",
    "/licences-llcer-brochures",
    "/masters-llcer-brochures",
)

INALCO_CURATED_FORMATION_PATHS = (
    "/formations/licence-llcer-parcours-bilangue",
    "/formations/licence-llcer-parcours-professionnalisant",
    "/formations/licences-llcer-parcours-thematiques-et-disciplinaires",
    "/formations/master-ti-traduction-specialisee",
    "/formations/master-traitement-automatique-des-langues-tal",
)

INALCO_ALLOWED_PATHS = (*INALCO_CORE_PATHS, *INALCO_CURATED_FORMATION_PATHS)
INALCO_TEMPORAL_EXACT_PATHS = (
    "/candidatures",
    "/candidater-un-cursus-diplomant",
    "/inscriptions-administratives",
    "/reglements-et-chartes-etudiantes",
    "/schema-directeur-de-la-vie-etudiante",
    "/ddrse",
)

PDF_SOURCES = (
    {
        "source_url": (
            "https://www.inalco.fr/sites/default/files/2024-05/"
            "Sh%C3%A9ma%20Directeur%20de%20la%20Vie%20"
            "%C3%89tudiante-avec%20compression.pdf"
        ),
        "parent_url": "https://www.inalco.fr/schema-directeur-de-la-vie-etudiante",
        "title": "Schéma Directeur de la Vie Étudiante 2023-2028",
        "validity_period": "2023-2028",
        "knowledge_type": "temporal",
    },
    {
        "source_url": (
            "https://www.inalco.fr/sites/default/files/2025-06/"
            "Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf"
        ),
        "parent_url": "https://www.inalco.fr/ddrse",
        "title": "Schéma Directeur DD&RSE 2025-2030",
        "validity_period": "2025-2030",
        "knowledge_type": "temporal",
    },
)

MAX_PDF_BYTES = 25 * 1024 * 1024
PDF_REQUEST_TIMEOUT = 90

INALCO_SEED_URLS = [
    f"https://www.inalco.fr{path}" for path in INALCO_ALLOWED_PATHS
]

SEED_URLS = [PORTAIL_BASE_URL, PORTAIL_SITE_MAP_URL, *INALCO_SEED_URLS]

SOURCE_PROFILES = {
    "portail-etudiant.inalco.fr": {
        "source_scope": "official_student_portal",
        "source_priority": 1.0,
        "crawl_links": True,
        "allowed_exact_paths": (),
        "allowed_path_prefixes": ("/fr/",),
        "excluded_paths": (
            "/fr/footer/inalco-fr.html",
            "/fr/footer/autres-liens/politique-de-confidentialite.html",
            "/fr/etudes/accompagnement-vers-la-reussite/direction-d-etudes.html",
        ),
        "temporal_path_prefixes": (
            "/fr/actualites/",
            "/fr/evenements/",
        ),
        "low_priority_path_prefixes": (
            "/fr/autres/aide/",
            "/fr/footer/",
        ),
    },
    "www.inalco.fr": {
        "source_scope": "official_institutional_site",
        "source_priority": 1.15,
        # Keep institutional pages as an explicit whitelist. Add more exact
        # pages only when they answer an evaluation question.
        "crawl_links": False,
        "allowed_exact_paths": INALCO_ALLOWED_PATHS,
        "allowed_path_prefixes": (),
        "excluded_paths": (),
        "temporal_exact_paths": INALCO_TEMPORAL_EXACT_PATHS,
        "temporal_path_prefixes": (),
        "low_priority_path_prefixes": (),
    },
    "inalco.fr": {
        "source_scope": "official_institutional_site",
        "source_priority": 1.15,
        "crawl_links": False,
        "allowed_exact_paths": INALCO_ALLOWED_PATHS,
        "allowed_path_prefixes": (),
        "excluded_paths": (),
        "temporal_exact_paths": INALCO_TEMPORAL_EXACT_PATHS,
        "temporal_path_prefixes": (),
        "low_priority_path_prefixes": (),
    },
}

EXCLUDED_EXTENSIONS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    ".css",
    ".js",
    ".zip",
    ".mp4",
    ".webm",
    ".ico",
)

MAX_PAGES = 1200
REQUEST_TIMEOUT = 15
CRAWL_DELAY = 0.3
MIN_PAGE_CHARS = 100

CHUNK_MAX_CHARS = 1500
CHUNK_MIN_CHARS = 200
MIN_INDEXABLE_CHARS = 40
SHORT_CHUNK_CHARS = 200
SHORT_CHUNK_PRIORITY_FACTOR = 0.7

INVALID_CONTENT_PATTERNS = (
    "comment déposer un pdf",
    "ne remonte pas dans les recherches",
)

PLACEHOLDER_CONTENT = (
    "carence",
    "en attente",
    "en cours de construction",
)

USER_AGENT = "InalcoStudentChatbotResearch/0.2 (+academic project)"
