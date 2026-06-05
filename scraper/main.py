from crawler import crawl_site
from extractor import extract_page
from cleaner import clean_page
from chunker import build_chunks
from metadata import enrich_chunk
from storage import save_jsonl


def main():
    urls = crawl_site()

    pages = []
    chunks = []

    for url in urls:
        page = extract_page(url)

        if not page:
            continue

        page = clean_page(page)
        pages.append(page)

        for chunk in build_chunks(page):
            chunks.append(enrich_chunk(chunk))

    save_jsonl(pages, "data/pages.jsonl")
    save_jsonl(chunks, "data/chunks.jsonl")

    print(f"Saved {len(pages)} pages")
    print(f"Saved {len(chunks)} chunks")


if __name__ == "__main__":
    main()