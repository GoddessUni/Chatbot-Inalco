import re

def clean_text(text: str) -> str:
    text = text.replace("\xa0", " ")

    # Conserve les étiquettes ou adresses mail utiles et enlève les liens JavaScript non navigable.
    text = re.sub(
        r"\[([^\]]+)\]\(javascript:void\(0\)\)",
        r"\1",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"javascript:void\(0\)", "", text, flags=re.IGNORECASE)

    # Le portal affiche les adresses mail avec les espaces
    text = re.sub(
        r"\b([\w.+-]+)\s*@\s*([\w.-]+\.[A-Za-z]{2,})\b",
        r"\1@\2",
        text,
    )

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def clean_page(page: dict) -> dict:
    page = dict(page)
    page["title"] = clean_text(page.get("title", ""))
    page["html_title"] = clean_text(page.get("html_title", ""))
    page["text"] = clean_text(page["text"])
    page["sections"] = [
        {
            "section_title": clean_text(section.get("section_title", "")),
            "text": clean_text(section.get("text", "")),
        }
        for section in page.get("sections", [])
        if clean_text(section.get("text", ""))
    ]
    return page
