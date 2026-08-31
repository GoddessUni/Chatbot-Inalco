import hashlib
import math
import re
from collections import Counter


TOKEN_PATTERN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9']{2,}", re.UNICODE)


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text or "")]


def _bucket(token: str, dim: int) -> tuple[int, float]:
    digest = hashlib.blake2b(token.encode("utf-8"), digest_size=8).digest()
    value = int.from_bytes(digest, "big")
    index = value % dim
    sign = 1.0 if (value >> 63) == 0 else -1.0
    return index, sign


def embed_text(text: str, dim: int = 768) -> list[float]:
    counts = Counter(tokenize(text))
    vector = [0.0] * dim

    for token, count in counts.items():
        index, sign = _bucket(token, dim)
        vector[index] += sign * (1.0 + math.log(count))

    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [round(value / norm, 6) for value in vector]


def cosine(vector_a: list[float], vector_b: list[float]) -> float:
    if not vector_a or not vector_b:
        return 0.0
    return sum(a * b for a, b in zip(vector_a, vector_b))
