import hashlib
import re
from urllib.parse import urlparse


def normalize_for_hash(text: str) -> str:
    return re.sub(r"\W+", " ", text.lower()).strip()


def content_hash(text: str) -> str:
    normalized = normalize_for_hash(text)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _preference_score(record: dict) -> tuple:
    path = urlparse(record.get("source_url", "")).path
    path_depth = len([part for part in path.split("/") if part])
    return (
        record.get("retrieval_priority", 1.0),
        path_depth,
        bool(record.get("title")),
        len(record.get("text", "")),
    )


def deduplicate_records(records: list[dict]) -> tuple[list[dict], list[dict]]:
    groups = {}
    duplicates = []

    for record in records:
        record = dict(record)
        digest = content_hash(record["text"])
        record["content_hash"] = digest
        groups.setdefault(digest, []).append(record)

    unique = []
    for digest, group in groups.items():
        preferred = max(group, key=_preference_score)
        unique.append(preferred)

        for record in group:
            if record is preferred:
                continue
            duplicates.append(
                {
                    "source_url": record.get("source_url"),
                    "duplicate_of": preferred.get("source_url"),
                    "content_hash": digest,
                }
            )

    return unique, duplicates
