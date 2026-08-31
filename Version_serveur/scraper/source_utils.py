from urllib.parse import urlparse

from config import SOURCE_PROFILES


def get_source_profile(url: str) -> dict | None:
    parsed = urlparse(url)
    return SOURCE_PROFILES.get(parsed.netloc)


def get_source_domain(url: str) -> str:
    return urlparse(url).netloc


def get_source_scope(url: str) -> str:
    profile = get_source_profile(url)
    return profile["source_scope"] if profile else "unknown"


def get_source_priority(url: str) -> float:
    profile = get_source_profile(url)
    return profile.get("source_priority", 1.0) if profile else 1.0


def is_known_source(url: str) -> bool:
    return get_source_profile(url) is not None


def path_matches_any(path: str, patterns: tuple[str, ...]) -> bool:
    return any(pattern in path for pattern in patterns)
