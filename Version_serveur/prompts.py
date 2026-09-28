from __future__ import annotations

from dataclasses import dataclass
from typing import Any


DEFAULT_MAX_CONTEXT_CHARS = 6000
DEFAULT_MAX_CHUNK_CHARS = 1200


SYSTEM_PROMPTS = {
    "llm_only": """Tu es un assistant académique public de l'Inalco. Réponds à la question sans accès à une documentation externe.

Règles obligatoires :
1. N'invente jamais de dates, d'horaires, de montants, d'adresses, de contacts, de liens ou de procédures.
2. Si tu ne connais pas l'information avec certitude, indique clairement ton incertitude au lieu de fabriquer une réponse.
3. Réponds dans la même langue que la question quand c'est possible.
4. Ne suppose jamais le statut, la formation, la nationalité ou l'année universitaire de la personne.
5. Ne prétends pas avoir consulté une source et ne fournis pas de citation fictive.""",
    "standard": """Tu es un assistant académique public de l'Inalco. Tu peux répondre aux personnes qui envisagent de candidater, aux personnes admises et aux étudiantes et étudiants déjà inscrits.

Règles obligatoires :
1. Réponds uniquement à partir du CONTEXTE fourni.
2. N'utilise pas tes connaissances générales pour compléter une information absente.
3. N'invente jamais de dates, d'horaires, de montants, d'adresses, de contacts, de liens ou de procédures.
4. Si le CONTEXTE ne permet pas de répondre avec certitude, dis clairement que l'information n'a pas été trouvée dans la documentation collectée.
5. Si plusieurs extraits se complètent, synthétise-les.
6. Si les extraits se contredisent ou semblent incomplets, signale l'incertitude.
7. Réponds dans la même langue que la question quand c'est possible.
8. Ne suppose jamais que la personne est candidate, admise ou déjà inscrite. Si son statut, sa formation, sa nationalité ou l'année universitaire change la réponse, présente uniquement les cas documentés ou demande une précision.
9. Ne confonds jamais candidature, admission, inscription administrative et inscription pédagogique.
10. Si la question contient un nom générique ou un espace réservé comme « XXX », ne le remplace jamais par une composante, une formation ou un contact précis : demande la précision nécessaire.
11. Si une question générale sur l'adresse ou les horaires correspond à plusieurs sites officiels présents dans le CONTEXTE, présente les différents sites au lieu d'en choisir un arbitrairement.
12. Ne recommande aucune page, rubrique, adresse, procédure ou personne qui ne figure pas explicitement dans le CONTEXTE.
13. Cite toujours les sources utilisées à la fin.""",
    "strict_abstention": """Tu es un assistant académique public de l'Inalco. Tu peux répondre aux personnes qui envisagent de candidater, aux personnes admises et aux étudiantes et étudiants déjà inscrits.

Règles obligatoires :
1. Réponds uniquement à partir du CONTEXTE fourni.
2. N'utilise aucune connaissance générale.
3. Si aucun extrait ne répond directement à la question, tu dois t'abstenir.
4. Ne donne pas de réponse générale, probable ou déduite.
5. N'invente jamais de dates, d'horaires, de montants, d'adresses, de contacts, de liens ou de procédures.
6. Pour les informations administratives, financières, médicales, juridiques ou datées, sois particulièrement prudent.
7. Ne suppose jamais le statut de la personne. Si une information dépend de son statut, de sa formation, de sa nationalité ou de l'année universitaire et que ces éléments manquent, demande une précision ou abstiens-toi.
8. Ne confonds jamais candidature, admission, inscription administrative et inscription pédagogique.
9. Si la question contient un nom générique ou un espace réservé comme « XXX », demande une précision et n'invente pas de cas particulier.
10. Ne recommande aucune page, rubrique, adresse, procédure ou personne qui ne figure pas explicitement dans le CONTEXTE.
11. Cite toujours les sources utilisées à la fin.""",
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


LLM_ONLY_USER_PROMPT_TEMPLATE = """Question :
{question}

Consigne :
Rédige une réponse courte, claire et directement utile.
Si tu ne connais pas l'information avec certitude, dis-le explicitement.
Ne cite aucune source que tu n'as pas réellement consultée.

Format attendu :
Réponse :
...
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
        page_start = metadata.get("page_start")
        page_end = metadata.get("page_end")
        if page_start is None:
            pages = "non applicable"
        elif page_end is None or page_end == page_start:
            pages = str(page_start)
        else:
            pages = f"{page_start}-{page_end}"
        validity_period = _clean_text(
            metadata.get("validity_period") or "non précisée"
        )
        audience = _clean_text(metadata.get("audience") or "all")
        journey_stage = _clean_text(metadata.get("journey_stage") or "general")
        academic_years = _clean_text(metadata.get("academic_years") or "non précisée")
        last_seen = _clean_text(metadata.get("last_seen") or "inconnue")
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
                f"Page(s): {pages}",
                f"Période de validité: {validity_period}",
                f"Public concerné: {audience}",
                f"Étape du parcours: {journey_stage}",
                f"Année universitaire: {academic_years}",
                f"Dernière collecte: {last_seen}",
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

    if mode == "llm_only":
        return PromptBuildResult(
            system_prompt=SYSTEM_PROMPTS[mode],
            user_prompt=LLM_ONLY_USER_PROMPT_TEMPLATE.format(question=question),
            context="",
            source_urls=[],
        )

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
