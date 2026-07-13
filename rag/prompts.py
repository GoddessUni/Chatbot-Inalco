from __future__ import annotations

from dataclasses import dataclass
from typing import Any


DEFAULT_MAX_CONTEXT_CHARS = 6000
DEFAULT_MAX_CHUNK_CHARS = 1200


SYSTEM_PROMPTS = {
    "standard": """Tu es un assistant académique destiné aux étudiantes et étudiants de l'Inalco.

Règles obligatoires :
1. Réponds uniquement à partir du CONTEXTE fourni.
2. N'utilise pas tes connaissances générales pour compléter une information absente.
3. N'invente jamais de dates, d'horaires, de montants, d'adresses, de contacts, de liens ou de procédures.
4. Si le CONTEXTE ne permet pas de répondre avec certitude, dis clairement que l'information n'a pas été trouvée dans la documentation collectée.
5. Si plusieurs extraits se complètent, synthétise-les.
6. Si les extraits se contredisent ou semblent incomplets, signale l'incertitude.
7. Réponds dans la même langue que la question quand c'est possible.
8. Cite toujours les sources utilisées à la fin.""",
    "strict_abstention": """Tu es un assistant académique destiné aux étudiantes et étudiants de l'Inalco.

Règles obligatoires :
1. Réponds uniquement à partir du CONTEXTE fourni.
2. N'utilise aucune connaissance générale.
3. Si aucun extrait ne répond directement à la question, tu dois t'abstenir.
4. Ne donne pas de réponse générale, probable ou déduite.
5. N'invente jamais de dates, d'horaires, de montants, d'adresses, de contacts, de liens ou de procédures.
6. Pour les informations administratives, financières, médicales, juridiques ou datées, sois particulièrement prudent.
7. Cite toujours les sources utilisées à la fin.""",
}


USER_PROMPT_TEMPLATE = """Question de l'étudiant :
{question}

CONTEXTE :
{context}

Consigne :
Rédige une réponse courte, claire et directement utile pour un étudiant.
Utilise uniquement les informations présentes dans le CONTEXTE.
Si le contexte est insuffisant, réponds exactement :
"Je n'ai pas trouvé cette information dans la documentation collectée."

Format attendu :
Réponse :
...

Sources :
- ...
"""


@dataclass(frozen=True)
class PromptBuildResult:
    system_prompt: str
    user_prompt: str
    context: str
    source_urls: list[str]

    def as_messages(self) -> list[dict[str, str]]:
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt},
        ]

    def as_text_prompt(self) -> str:
        return (
            "SYSTEM:\n"
            f"{self.system_prompt}\n\n"
            "USER:\n"
            f"{self.user_prompt}"
        )


def _clean_text(value: Any) -> str:
    return str(value or "").replace("\r", " ").strip()


def _truncate(text: str, max_chars: int) -> str:
    text = _clean_text(text)
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "..."


def _metadata(hit: dict) -> dict:
    return hit.get("metadata", {}) or {}


def source_url_for(hit: dict) -> str:
    metadata = _metadata(hit)
    return _clean_text(metadata.get("source_url") or "source inconnue")


def format_context(
    hits: list[dict],
    max_context_chars: int = DEFAULT_MAX_CONTEXT_CHARS,
    max_chunk_chars: int = DEFAULT_MAX_CHUNK_CHARS,
    include_scores: bool = True,
) -> str:
    blocks = []
    current_size = 0

    for rank, hit in enumerate(hits, start=1):
        metadata = _metadata(hit)
        title = _clean_text(metadata.get("title") or "Sans titre")
        section = _clean_text(metadata.get("section_title") or "Sans section")
        url = source_url_for(hit)
        quality = _clean_text(metadata.get("quality_status") or "unknown")
        review_priority = _clean_text(metadata.get("review_priority") or "none")
        source_type = _clean_text(metadata.get("source_type") or "unknown")
        text = _truncate(hit.get("text") or "", max_chunk_chars)

        score_lines = []
        if include_scores:
            score_lines.append(f"Score de récupération: {hit.get('score', 'n/a')}")
            if "semantic_score" in hit:
                score_lines.append(f"Score sémantique: {hit.get('semantic_score')}")

        block = "\n".join(
            [
                f"[Source {rank}]",
                f"Titre: {title}",
                f"Section: {section}",
                f"URL: {url}",
                f"Type de source: {source_type}",
                f"Statut qualité: {quality} / {review_priority}",
                *score_lines,
                "Extrait:",
                text,
            ]
        )

        projected_size = current_size + len(block) + 2
        if blocks and projected_size > max_context_chars:
            break

        blocks.append(block)
        current_size = projected_size

    if not blocks:
        return "Aucun extrait pertinent n'a été récupéré."

    return "\n\n".join(blocks)


def unique_source_urls(hits: list[dict]) -> list[str]:
    urls = []
    seen = set()
    for hit in hits:
        url = source_url_for(hit)
        if url and url not in seen:
            urls.append(url)
            seen.add(url)
    return urls


def build_prompt(
    question: str,
    hits: list[dict],
    mode: str = "standard",
    max_context_chars: int = DEFAULT_MAX_CONTEXT_CHARS,
    max_chunk_chars: int = DEFAULT_MAX_CHUNK_CHARS,
    include_scores: bool = True,
) -> PromptBuildResult:
    if mode not in SYSTEM_PROMPTS:
        allowed = ", ".join(sorted(SYSTEM_PROMPTS))
        raise ValueError(f"Unknown prompt mode: {mode}. Allowed modes: {allowed}")

    context = format_context(
        hits,
        max_context_chars=max_context_chars,
        max_chunk_chars=max_chunk_chars,
        include_scores=include_scores,
    )
    user_prompt = USER_PROMPT_TEMPLATE.format(question=question, context=context)

    return PromptBuildResult(
        system_prompt=SYSTEM_PROMPTS[mode],
        user_prompt=user_prompt,
        context=context,
        source_urls=unique_source_urls(hits),
    )


def should_abstain(
    hits: list[dict],
    min_top_score: float = 0.72,
    min_semantic_score: float | None = None,
) -> tuple[bool, str | None]:
    if not hits:
        return True, "no_retrieval_hit"

    top = hits[0]
    if float(top.get("score", 0.0)) < min_top_score:
        return True, "top_score_below_threshold"

    if min_semantic_score is not None:
        semantic_score = float(top.get("semantic_score", top.get("score", 0.0)))
        if semantic_score < min_semantic_score:
            return True, "semantic_score_below_threshold"

    return False, None

