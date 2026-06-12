import argparse
from pathlib import Path

from chunker import build_chunks
from cleaner import clean_page
from crawler import crawl_site
from deduplicate import mark_duplicate_pages, merge_duplicate_chunks
from extractor import extract_page
from metadata import enrich_chunk
from page_filter import classify_page
from quality import assess_chunk, assess_page, build_review_record
from storage import save_jsonl


def build_knowledge_base(output_dir: str) -> None:
    output = Path(output_dir)
    urls, crawl_failures = crawl_site()

    pages = []
    extraction_failures = []
    rejected_pages = []

    for index, url in enumerate(urls, start=1):
        print(f"[{index}/{len(urls)}] Extracting {url}")
        page = extract_page(url)

        if not page:
            extraction_failures.append(
                {"url": url, "stage": "extract", "error": "No usable text extracted"}
            )
            continue

        page = clean_page(page)
        page = classify_page(page)

        accepted, reasons = assess_page(page)
        if not accepted:
            rejected_pages.append(
                {
                    "source_url": page["source_url"],
                    "title": page.get("title"),
                    "rejection_reasons": reasons,
                }
            )
            continue

        pages.append(page)

    pages, page_duplicates = mark_duplicate_pages(pages)

    chunks = []
    for page in pages:
        chunks.extend(enrich_chunk(chunk) for chunk in build_chunks(page))

    chunks, chunk_duplicates = merge_duplicate_chunks(chunks)
    indexable_chunks = []
    rejected_chunks = []
    review_queue = []

    for chunk in chunks:
        assessed_chunk, rejection_reasons, _ = assess_chunk(chunk)

        if rejection_reasons:
            rejected_chunks.append(
                {
                    "chunk_id": chunk.get("chunk_id"),
                    "source_url": chunk.get("source_url"),
                    "title": chunk.get("title"),
                    "section_title": chunk.get("section_title"),
                    "text": chunk.get("text"),
                    "rejection_reasons": rejection_reasons,
                }
            )
            continue

        indexable_chunks.append(assessed_chunk)
        review_record = build_review_record(assessed_chunk)
        if review_record:
            review_queue.append(review_record)

    save_jsonl(pages, str(output / "pages.jsonl"))
    save_jsonl(indexable_chunks, str(output / "chunks.jsonl"))
    save_jsonl(crawl_failures + extraction_failures, str(output / "failures.jsonl"))
    save_jsonl(page_duplicates, str(output / "page_duplicates.jsonl"))
    save_jsonl(chunk_duplicates, str(output / "chunk_duplicates.jsonl"))
    save_jsonl(rejected_pages, str(output / "rejected_pages.jsonl"))
    save_jsonl(rejected_chunks, str(output / "rejected_chunks.jsonl"))
    save_jsonl(review_queue, str(output / "review_queue.jsonl"))

    print()
    print(f"Discovered URLs: {len(urls)}")
    print(f"Extracted pages: {len(pages)}")
    print(f"Unique chunks before quality filtering: {len(chunks)}")
    print(f"Indexable chunks: {len(indexable_chunks)}")
    print(f"Failures: {len(crawl_failures) + len(extraction_failures)}")
    print(f"Duplicate pages marked: {len(page_duplicates)}")
    print(f"Duplicate chunks removed: {len(chunk_duplicates)}")
    print(f"Rejected pages: {len(rejected_pages)}")
    print(f"Rejected chunks: {len(rejected_chunks)}")
    print(f"Review queue: {len(review_queue)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="data")
    args = parser.parse_args()
    build_knowledge_base(args.output_dir)
