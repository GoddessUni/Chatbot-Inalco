from datetime import date
from bs4 import BeautifulSoup
import trafilatura


def extract_page(url: str) -> dict | None:
    downloaded = trafilatura.fetch_url(url)

    if not downloaded:
        return None

    text = trafilatura.extract(
        downloaded,
        include_links=True,
        include_tables=True,
        favor_precision=True
    )

    if not text or len(text.strip()) < 100:
        return None

    soup = BeautifulSoup(downloaded, "html.parser")

    title = soup.title.get_text(" ", strip=True) if soup.title else ""

    h1 = soup.find("h1")
    main_title = h1.get_text(" ", strip=True) if h1 else title

    return {
        "source_url": url,
        "title": main_title,
        "html_title": title,
        "language": "fr",
        "content_type": "web_page",
        "last_seen": str(date.today()),
        "text": text
    }