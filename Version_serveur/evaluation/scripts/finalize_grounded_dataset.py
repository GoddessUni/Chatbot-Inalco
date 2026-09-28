from __future__ import annotations

import argparse
import csv
import json
from datetime import date
from pathlib import Path


TRUE_VALUES = {"1", "true", "yes", "oui"}
FALSE_VALUES = {"0", "false", "no", "non"}
ALLOWED_BEHAVIORS = {"answer", "abstain", "clarify"}
ALLOWED_SPLITS = {"pilot", "validation", "test"}


def parse_bool(value: str, field: str, question_id: str) -> bool:
    normalized = (value or "").strip().lower()
    if normalized in TRUE_VALUES:
        return True
    if normalized in FALSE_VALUES:
        return False
    raise ValueError(f"{question_id}: invalid {field}: {value!r}")


def parse_ranks(value: str) -> list[int]:
    if not (value or "").strip():
        return []
    return sorted({int(item.strip()) for item in value.split(",") if item.strip()})


def parse_facts(value: str, question_id: str) -> list[dict]:
    facts = [item.strip() for item in (value or "").split("||") if item.strip()]
    return [
        {"fact_id": f"{question_id}_f{number}", "text": fact}
        for number, fact in enumerate(facts, start=1)
    ]


def evidence_from_rank(row: dict, rank: int) -> dict:
    prefix = f"candidate_{rank}_"
    url = (row.get(prefix + "url") or "").strip()
    if not url:
        raise ValueError(f"{row['question_id']}: candidate rank {rank} has no URL")
    page = (row.get(prefix + "page") or "").strip()
    page_start = None
    page_end = None
    if page:
        parts = page.split("-", maxsplit=1)
        page_start = int(parts[0])
        page_end = int(parts[1]) if len(parts) == 2 else page_start
    return {
        "source_url": url,
        "title": (row.get(prefix + "title") or "").strip() or None,
        "section_title": (row.get(prefix + "section") or "").strip() or None,
        "page_start": page_start,
        "page_end": page_end,
        "candidate_rank": rank,
        "verified_against_source": True,
    }


def manual_evidence(row: dict) -> dict | None:
    url = (row.get("manual_source_url") or "").strip()
    if not url:
        return None
    page = (row.get("manual_source_page") or "").strip()
    page_start = None
    page_end = None
    if page:
        parts = page.split("-", maxsplit=1)
        page_start = int(parts[0])
        page_end = int(parts[1]) if len(parts) == 2 else page_start
    return {
        "source_url": url,
        "title": (row.get("manual_source_title") or "").strip() or None,
        "section_title": (row.get("manual_source_section") or "").strip() or None,
        "page_start": page_start,
        "page_end": page_end,
        "candidate_rank": None,
        "verified_against_source": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate a reviewed CSV and create the final evaluation JSONL."
    )
    parser.add_argument("--review-csv", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    records = []
    errors = []
    with args.review_csv.open(encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            question_id = (row.get("question_id") or "").strip()
            try:
                answerable_by_site = parse_bool(
                    row.get("answerable_by_official_site", ""),
                    "answerable_by_official_site",
                    question_id,
                )
                answerable_by_kb = parse_bool(
                    row.get("answerable_by_kb", ""),
                    "answerable_by_kb",
                    question_id,
                )
                clarify = parse_bool(
                    row.get("requires_clarification", ""),
                    "requires_clarification",
                    question_id,
                )
                behavior = (row.get("expected_behavior") or "").strip().lower()
                if behavior not in ALLOWED_BEHAVIORS:
                    raise ValueError(
                        f"{question_id}: expected_behavior must be one of "
                        f"{sorted(ALLOWED_BEHAVIORS)}"
                    )
                split = (row.get("split") or "").strip().lower()
                if split not in ALLOWED_SPLITS:
                    raise ValueError(
                        f"{question_id}: split must be one of {sorted(ALLOWED_SPLITS)}"
                    )
                ranks = parse_ranks(row.get("gold_candidate_ranks", ""))
                facts = parse_facts(row.get("gold_facts", ""), question_id)
                extra_evidence = manual_evidence(row)

                if answerable_by_kb and not answerable_by_site:
                    raise ValueError(
                        f"{question_id}: KB cannot be answerable when the official site is not"
                    )
                if behavior == "answer" and not answerable_by_kb:
                    raise ValueError(
                        f"{question_id}: answer behavior requires answerable_by_kb=true"
                    )
                if behavior == "answer" and (not (ranks or extra_evidence) or not facts):
                    raise ValueError(
                        f"{question_id}: answer behavior requires evidence and gold facts"
                    )
                if behavior == "abstain" and answerable_by_kb:
                    raise ValueError(
                        f"{question_id}: abstain behavior requires answerable_by_kb=false"
                    )
                if behavior == "clarify" and not clarify:
                    raise ValueError(
                        f"{question_id}: clarify behavior requires requires_clarification=true"
                    )
                if not (row.get("source_verified_at") or "").strip():
                    raise ValueError(f"{question_id}: source_verified_at is required")
                if not (row.get("annotator") or "").strip():
                    raise ValueError(f"{question_id}: annotator is required")

                evidence = [evidence_from_rank(row, rank) for rank in ranks]
                if extra_evidence:
                    evidence.append(extra_evidence)

                records.append(
                    {
                        "question_id": question_id,
                        "question": (row.get("question") or "").strip(),
                        "category": (row.get("category") or "general").strip(),
                        "risk_level": (row.get("risk_level") or "low").strip(),
                        "split": split,
                        "answerable": answerable_by_kb,
                        "answerable_by_official_site": answerable_by_site,
                        "answerable_by_kb": answerable_by_kb,
                        "requires_clarification": clarify,
                        "expected_behavior": behavior,
                        "gold_facts": facts,
                        "gold_evidence": evidence,
                        "verification_status": "human_verified",
                        "source_verified_at": row["source_verified_at"].strip(),
                        "annotator": row["annotator"].strip(),
                        "finalized_at": str(date.today()),
                        "notes": (row.get("notes") or "").strip() or None,
                    }
                )
            except (TypeError, ValueError) as exc:
                errors.append(str(exc))

    if errors:
        print("Dataset validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as file:
        for record in records:
            file.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"Records: {len(records)}")
    print(f"Final dataset: {args.output}")


if __name__ == "__main__":
    main()
