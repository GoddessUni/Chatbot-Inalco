# Prototype RAG local

Ce dossier permet de tester rapidement un prototype RAG sans dependances externes.
Les chunks en attente de verification sont traites comme utilisables uniquement pour
les essais, tout en conservant `quality_status`, `review_priority` et `quality_flags`.

## Construire la base prototype

```bash
cd /Users/dingdingcheng/chatbot-Inalco_v0.3
source .venv/bin/activate

python rag/prototype_kb.py \
  --input data_multisite_strict/kb/all_indexable_with_embedding_text.jsonl \
  --output data_multisite_strict/kb/prototype_all_trusted.jsonl
```

## Construire l'index

```bash
python rag/build_index.py \
  --input data_multisite_strict/kb/prototype_all_trusted.jsonl \
  --output indexes/prototype_hash/index.jsonl
```

## Tester la recherche

```bash
python rag/retrieve.py "Ou puis-je manger pres de l'Inalco ?"
python rag/retrieve.py "Comment demander une bourse ?"
python rag/retrieve.py "Comment trouver un logement ?"
```

## Tester le chatbot prototype

```bash
python rag/chatbot.py "Ou puis-je manger pres de l'Inalco ?"
```

La version actuelle utilise un embedding lexical par hashing. Elle sert a tester la
chaine RAG et les donnees collectees. Pour une version plus semantique, remplacer
`hash_embedder.py` par un backend `sentence-transformers`, OpenAI embeddings,
Chroma ou FAISS.
