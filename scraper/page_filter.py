from urllib.parse import urlparse

from config import LOW_PRIORITY_PATH_PREFIXES, TEMPORAL_PATH_PREFIXES


def classify_page(page: dict) -> dict:
    page = dict(page)
    path = urlparse(page["source_url"]).path

    if any(path.startswith(prefix) for prefix in TEMPORAL_PATH_PREFIXES):
        knowledge_type = "temporal"
        retrieval_priority = 0.5
    elif any(path.startswith(prefix) for prefix in LOW_PRIORITY_PATH_PREFIXES):
        knowledge_type = "portal_help"
        retrieval_priority = 0.7
    else:
        knowledge_type = "stable"
        retrieval_priority = 1.0

    page.update(
        {
            "knowledge_type": knowledge_type,
            "retrieval_priority": retrieval_priority,
            "source_type": "official_web_page",
            "scraped_successfully": True,
            "human_verified": False,
        }
    )
    return page
