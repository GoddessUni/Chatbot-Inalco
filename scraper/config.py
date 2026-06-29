PORTAIL_BASE_URL = "https://portail-etudiant.inalco.fr/fr/index.html"
PORTAIL_SITE_MAP_URL = (
    "https://portail-etudiant.inalco.fr/fr/footer/autres-liens/plan-du-site.html"
)

INALCO_SEED_URLS = [
    "https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription",
    "https://www.inalco.fr/faq-admission-en-master",
    "https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement",
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
        "allowed_exact_paths": (
            "/foire-aux-questions-faq-procedure-dinscription",
            "/faq-admission-en-master",
            "/droits-de-scolarite-tarifs-exoneration-annulation-remboursement",
        ),
        "allowed_path_prefixes": (),
        "excluded_paths": (),
        "temporal_path_prefixes": (),
        "low_priority_path_prefixes": (),
    },
    "inalco.fr": {
        "source_scope": "official_institutional_site",
        "source_priority": 1.15,
        "crawl_links": False,
        "allowed_exact_paths": (
            "/foire-aux-questions-faq-procedure-dinscription",
            "/faq-admission-en-master",
            "/droits-de-scolarite-tarifs-exoneration-annulation-remboursement",
        ),
        "allowed_path_prefixes": (),
        "excluded_paths": (),
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
