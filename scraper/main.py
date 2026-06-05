import argparse
from pathlib import Path

from chunker import build_chunks
from cleaner import clean_page
from crawler import crawl_site
from deduplicate import deduplicate_records
from extractor import extract_page
from metadata import enrich_chunk
from page_filter import classify_page
from storage import save_jsonl


def build_knowledge_base(output_dir: str) -> None:
    output = Path(output_dir)
    urls, crawl_failures = crawl_site()

    pages = []
    extraction_failures = []

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
        pages.append(page)

    pages, page_duplicates = deduplicate_records(pages)

    chunks = []
    for page in pages:
        chunks.extend(enrich_chunk(chunk) for chunk in build_chunks(page))

    chunks, chunk_duplicates = deduplicate_records(chunks)

    save_jsonl(pages, str(output / "pages.jsonl"))
    save_jsonl(chunks, str(output / "chunks.jsonl"))
    save_jsonl(crawl_failures + extraction_failures, str(output / "failures.jsonl"))
    save_jsonl(page_duplicates, str(output / "page_duplicates.jsonl"))
    save_jsonl(chunk_duplicates, str(output / "chunk_duplicates.jsonl"))

    print()
    print(f"Discovered URLs: {len(urls)}")
    print(f"Unique pages: {len(pages)}")
    print(f"Unique chunks: {len(chunks)}")
    print(f"Failures: {len(crawl_failures) + len(extraction_failures)}")
    print(f"Duplicate pages removed: {len(page_duplicates)}")
    print(f"Duplicate chunks removed: {len(chunk_duplicates)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="data")
    args = parser.parse_args()
    build_knowledge_base(args.output_dir)
