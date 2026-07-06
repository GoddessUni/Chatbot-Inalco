import argparse
import json
from collections import Counter
from pathlib import Path

from quality import review_priority
from storage import save_jsonl


def load_jsonl(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def compact(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item).strip() for item in value if str(item).strip())
    return str(value).strip()


def build_embedding_text(chunk: dict) -> str:
    """Build the text sent to embedding models, without changing source text."""
    fields = [
        ("Titre", chunk.get("title")),
        ("Section", chunk.get("section_title")),
        ("Theme", chunk.get("theme")),
        ("Type d'information", chunk.get("knowledge_type")),
        ("Niveau de risque", chunk.get("risk_level")),
        ("Domaine source", chunk.get("source_domain")),
        ("Portee source", chunk.get("source_scope")),
    ]

    lines = []
    for label, value in fields:
        text = compact(value)
        if text:
            lines.append(f"{label}: {text}")

    source_urls = chunk.get("source_urls") or [chunk.get("source_url")]
    source_text = compact(source_urls)
    if source_text:
        lines.append(f"Sources: {source_text}")

    lines.append("Contenu:")
    lines.append(compact(chunk.get("text")))
    return "\n".join(line for line in lines if line)


def prepare_kb_chunk(chunk: dict) -> dict:
    prepared = dict(chunk)
    priority = review_priority(prepared)
    prepared["review_priority"] = priority
    prepared["embedding_text"] = build_embedding_text(prepared)
    prepared["kb_partition"] = choose_partition(prepared)
    prepared["kb_indexable"] = prepared["kb_partition"] in {
        "main_ready",
        "stable_ready",
        "portal_help_ready",
        "temporal_separate",
        "review_p2_candidate",
    }
    return prepared


def choose_partition(chunk: dict) -> str:
    knowledge_type = chunk.get("knowledge_type")
    quality_status = chunk.get("quality_status")
    priority = chunk.get("review_priority") or review_priority(chunk)

    if quality_status == "ready" and knowledge_type in {"stable", "portal_help"}:
        return "main_ready"

    if knowledge_type == "temporal":
        return "temporal_separate"

    if priority == "P0":
        return "review_p0"

    if priority == "P1":
        return "review_p1"

    if priority == "P2":
        return "review_p2_candidate"

    if quality_status == "review":
        return "review_other"

    return "other"


def write_manifest(chunks: list[dict], output_dir: Path) -> None:
    manifest = {
        "total_chunks": len(chunks),
        "partitions": Counter(chunk.get("kb_partition") for chunk in chunks),
        "knowledge_types": Counter(chunk.get("knowledge_type") for chunk in chunks),
        "quality_statuses": Counter(chunk.get("quality_status") for chunk in chunks),
        "review_priorities": Counter(
            chunk.get("review_priority") or "none" for chunk in chunks
        ),
        "recommended_first_rag_files": [
            "kb/main_ready.jsonl",
            "kb/stable_ready.jsonl",
            "kb/portal_help_ready.jsonl",
        ],
        "use_with_caution": [
            "kb/temporal_separate.jsonl",
            "kb/review_p2_candidate.jsonl",
        ],
        "do_not_index_before_human_review": [
            "kb/review_p0.jsonl",
            "kb/review_p1.jsonl",
        ],
    }

    with (output_dir / "manifest.json").open("w", encoding="utf-8") as file:
        json.dump(manifest, file, ensure_ascii=False, indent=2)


def build_kb(chunks_path: str | Path, output_dir: str | Path) -> dict:
    output = Path(output_dir)
    chunks = [prepare_kb_chunk(chunk) for chunk in load_jsonl(chunks_path)]

    main_ready = [
        chunk
        for chunk in chunks
        if chunk["kb_partition"] == "main_ready"
    ]
    stable_ready = [
        chunk
        for chunk in main_ready
        if chunk.get("knowledge_type") == "stable"
    ]
    portal_help_ready = [
        chunk
        for chunk in main_ready
        if chunk.get("knowledge_type") == "portal_help"
    ]
    temporal = [
        chunk
        for chunk in chunks
        if chunk["kb_partition"] == "temporal_separate"
    ]
    review_all = [
        chunk
        for chunk in chunks
        if chunk.get("quality_status") == "review"
    ]
    review_p0 = [chunk for chunk in chunks if chunk.get("review_priority") == "P0"]
    review_p1 = [chunk for chunk in chunks if chunk.get("review_priority") == "P1"]
    review_p2 = [chunk for chunk in chunks if chunk.get("review_priority") == "P2"]

    save_jsonl(chunks, str(output / "all_indexable_with_embedding_text.jsonl"))
    save_jsonl(main_ready, str(output / "main_ready.jsonl"))
    save_jsonl(stable_ready, str(output / "stable_ready.jsonl"))
    save_jsonl(portal_help_ready, str(output / "portal_help_ready.jsonl"))
    save_jsonl(temporal, str(output / "temporal_separate.jsonl"))
    save_jsonl(review_all, str(output / "review_all.jsonl"))
    save_jsonl(review_p0, str(output / "review_p0.jsonl"))
    save_jsonl(review_p1, str(output / "review_p1.jsonl"))
    save_jsonl(review_p2, str(output / "review_p2_candidate.jsonl"))
    write_manifest(chunks, output)

    return {
        "total_chunks": len(chunks),
        "main_ready": len(main_ready),
        "stable_ready": len(stable_ready),
        "portal_help_ready": len(portal_help_ready),
        "temporal_separate": len(temporal),
        "review_all": len(review_all),
        "review_p0": len(review_p0),
        "review_p1": len(review_p1),
        "review_p2_candidate": len(review_p2),
    }


def print_summary(summary: dict) -> None:
    print()
    print("Knowledge base partitions:")
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chunks", default="data/chunks.jsonl")
    parser.add_argument("--output-dir", default="data/kb")
    args = parser.parse_args()
    print_summary(build_kb(args.chunks, args.output_dir))
