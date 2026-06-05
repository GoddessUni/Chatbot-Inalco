import re


def clean_text(text: str) -> str:
    text = text.replace("\xa0", " ")
    text = re.sub(
        r"\[([^\]]+)\]\(javascript:void\(0\)\)",
        r"\1",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"javascript:void\(0\)", "", text, flags=re.IGNORECASE)
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
    return page
