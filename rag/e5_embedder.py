import importlib.util
import os
from functools import lru_cache


DEFAULT_E5_MODEL = "intfloat/multilingual-e5-base"


def _require_sentence_transformers() -> None:
    if importlib.util.find_spec("sentence_transformers") is None:
        raise RuntimeError(
            "sentence-transformers is not installed. Install it with:\n"
            "  pip install sentence-transformers torch\n"
            "Then rebuild the E5 index."
        )


def choose_device() -> str:
    try:
        import torch

        if torch.cuda.is_available():
            return "cuda"
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "mps"
    except Exception:
        pass
    return "cpu"


@lru_cache(maxsize=2)
def load_model(model_name: str = DEFAULT_E5_MODEL):
    _require_sentence_transformers()
    previous_hf_offline = os.environ.get("HF_HUB_OFFLINE")
    previous_transformers_offline = os.environ.get("TRANSFORMERS_OFFLINE")

    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    from sentence_transformers import SentenceTransformer

    try:
        return SentenceTransformer(model_name, device=choose_device())
    except Exception:
        if previous_hf_offline is None:
            os.environ.pop("HF_HUB_OFFLINE", None)
        else:
            os.environ["HF_HUB_OFFLINE"] = previous_hf_offline

        if previous_transformers_offline is None:
            os.environ.pop("TRANSFORMERS_OFFLINE", None)
        else:
            os.environ["TRANSFORMERS_OFFLINE"] = previous_transformers_offline

        return SentenceTransformer(model_name, device=choose_device())


def normalize_for_e5(text: str, prefix: str) -> str:
    text = " ".join((text or "").split())
    if text.startswith(prefix):
        return text
    return f"{prefix}{text}"


def encode_passages(
    texts: list[str],
    model_name: str = DEFAULT_E5_MODEL,
    batch_size: int = 16,
) -> list[list[float]]:
    model = load_model(model_name)
    inputs = [normalize_for_e5(text, "passage: ") for text in texts]
    embeddings = model.encode(
        inputs,
        batch_size=batch_size,
        normalize_embeddings=True,
        show_progress_bar=True,
    )
    return embeddings.tolist()


def encode_query(question: str, model_name: str = DEFAULT_E5_MODEL) -> list[float]:
    model = load_model(model_name)
    embedding = model.encode(
        normalize_for_e5(question, "query: "),
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    return embedding.tolist()


def cosine(vector_a: list[float], vector_b: list[float]) -> float:
    if not vector_a or not vector_b:
        return 0.0
    return sum(a * b for a, b in zip(vector_a, vector_b))
