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
        1 if record.get("source_scope") == "official_institutional_site" else 0,
        path_depth,
        bool(record.get("title")),
        len(record.get("text", "")),
    )


def mark_duplicate_pages(records: list[dict]) -> tuple[list[dict], list[dict]]:
    groups = {}
    duplicates = []

    for record in records:
        record = dict(record)
        digest = content_hash(record["text"])
        record["content_hash"] = digest
        groups.setdefault(digest, []).append(record)

    marked = []
    for digest, group in groups.items():
        preferred = max(group, key=_preference_score)
        standard_url = preferred.get("source_url")

        for record in group:
            record["is_duplicate"] = record is not preferred
            record["duplicate_of"] = standard_url if record is not preferred else None
            record["standard_source_url"] = standard_url
            marked.append(record)

            if record is not preferred:
                duplicates.append(
                    {
                        "source_url": record.get("source_url"),
                        "duplicate_of": standard_url,
                        "content_hash": digest,
                    }
                )

    return marked, duplicates


def merge_duplicate_chunks(records: list[dict]) -> tuple[list[dict], list[dict]]:
    groups = {}
    duplicates = []

    for record in records:
        record = dict(record)
        digest = content_hash(record["text"])
        record["content_hash"] = digest
        groups.setdefault(digest, []).append(record)

    merged = []
    for digest, group in groups.items():
        preferred = max(group, key=_preference_score)
        standard_url = preferred.get("source_url")
        source_urls = sorted(
            {
                record.get("source_url")
                for record in group
                if record.get("source_url")
            }
        )
        source_domains = sorted(
            {
                record.get("source_domain")
                for record in group
                if record.get("source_domain")
            }
        )
        source_scopes = sorted(
            {
                record.get("source_scope")
                for record in group
                if record.get("source_scope")
            }
        )

        preferred["standard_source_url"] = standard_url
        preferred["source_url"] = standard_url
        preferred["source_urls"] = source_urls
        preferred["source_domains"] = source_domains
        preferred["source_scopes"] = source_scopes
        preferred["has_duplicate_sources"] = len(source_urls) > 1
        merged.append(preferred)

        for record in group:
            if record is preferred:
                continue
            duplicates.append(
                {
                    "chunk_id": record.get("chunk_id"),
                    "source_url": record.get("source_url"),
                    "duplicate_of_chunk_id": preferred.get("chunk_id"),
                    "standard_source_url": standard_url,
                    "content_hash": digest,
                }
            )

    return merged, duplicates
