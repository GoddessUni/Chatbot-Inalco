BASE_URL = "https://portail-etudiant.inalco.fr/fr/index.html"
SITE_MAP_URL = (
    "https://portail-etudiant.inalco.fr/fr/footer/autres-liens/plan-du-site.html"
)
SEED_URLS = [BASE_URL, SITE_MAP_URL]

ALLOWED_DOMAIN = "portail-etudiant.inalco.fr"
ALLOWED_PATH_PREFIX = "/fr/"

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

EXCLUDED_PATHS = (
    "/fr/footer/inalco-fr.html",
    "/fr/footer/autres-liens/politique-de-confidentialite.html",
)

TEMPORAL_PATH_PREFIXES = (
    "/fr/actualites/",
    "/fr/evenements/",
)

LOW_PRIORITY_PATH_PREFIXES = (
    "/fr/autres/aide/",
    "/fr/footer/",
)

MAX_PAGES = 1000
REQUEST_TIMEOUT = 15
CRAWL_DELAY = 0.3
MIN_PAGE_CHARS = 100

CHUNK_MAX_CHARS = 1500
CHUNK_MIN_CHARS = 200

USER_AGENT = "InalcoStudentChatbotResearch/0.2 (+academic project)"
