import argparse

from retrieve_e5 import retrieve


SYSTEM_LIMITATION = (
    "Prototype E5 local: les passages en attente de revue sont traites comme "
    "verifies pour les essais, mais leurs metadonnees restent affichees."
)


def answer(
    question: str,
    index_path: str,
    model_name: str,
    top_k: int,
    min_score: float,
) -> str:
    hits = retrieve(
        question,
        index_path=index_path,
        model_name=model_name,
        top_k=top_k,
        min_score=min_score,
    )
    if not hits:
        return (
            "Je n'ai pas trouve de source suffisamment pertinente dans la base "
            "collectee. Il faut verifier sur les sites officiels de l'Inalco ou du CROUS."
        )

    lines = [SYSTEM_LIMITATION, "", f"Question: {question}", "", "Elements trouves:"]
    for rank, hit in enumerate(hits, start=1):
        metadata = hit["metadata"]
        snippet = (hit.get("text") or "").replace("\n", " ")
        if len(snippet) > 650:
            snippet = snippet[:650].rstrip() + "..."

        lines.extend(
            [
                "",
                f"{rank}. {metadata.get('title') or 'Sans titre'}",
                f"   Section: {metadata.get('section_title') or 'Sans section'}",
                f"   Score: {hit['score']}",
                f"   Qualite: {metadata.get('quality_status')} / {metadata.get('review_priority')}",
                f"   Source: {metadata.get('source_url')}",
                f"   Extrait: {snippet}",
            ]
        )

    lines.extend(
        [
            "",
            "Reponse prototype:",
            "Ces passages sont les sources a transmettre au modele generateur.",
            "La reponse finale devra citer les URLs et s'abstenir si les extraits "
            "ne suffisent pas.",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--index", default="indexes/e5_base/index.jsonl")
    parser.add_argument("--model", default="intfloat/multilingual-e5-base")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-score", type=float, default=0.0)
    args = parser.parse_args()
    print(answer(args.question, args.index, args.model, args.top_k, args.min_score))


if __name__ == "__main__":
    main()
