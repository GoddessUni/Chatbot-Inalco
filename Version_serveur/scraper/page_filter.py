from urllib.parse import urlparse

from source_utils import get_source_priority, get_source_scope, get_source_domain


def classify_page(page: dict) -> dict:
    page = dict(page)
    parsed = urlparse(page["source_url"])
    path = parsed.path
    profile_scope = get_source_scope(page["source_url"])
    profile_priority = get_source_priority(page["source_url"])
    from config import SOURCE_PROFILES

    profile = SOURCE_PROFILES.get(parsed.netloc, {})

    if any(path.startswith(prefix) for prefix in profile.get("temporal_path_prefixes", ())):
        knowledge_type = "temporal"
        retrieval_priority = 0.5
    elif any(path.startswith(prefix) for prefix in profile.get("low_priority_path_prefixes", ())):
        knowledge_type = "portal_help"
        retrieval_priority = 0.7
    else:
        knowledge_type = "stable"
        retrieval_priority = 1.0

    retrieval_priority = round(retrieval_priority * profile_priority, 3)

    page.update(
        {
            "source_domain": get_source_domain(page["source_url"]),
            "source_scope": profile_scope,
            "knowledge_type": knowledge_type,
            "retrieval_priority": retrieval_priority,
            "source_type": "official_web_page",
            "scraped_successfully": True,
            "human_verified": False,
        }
    )
    return page
