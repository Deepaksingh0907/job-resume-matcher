from functools import lru_cache

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


@lru_cache
def get_embedding_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2"
    )


def calculate_semantic_similarity(
    resume_text: str,
    job_description: str
) -> float:
    if not resume_text.strip():
        return 0.0

    if not job_description.strip():
        return 0.0

    model = get_embedding_model()

    embeddings = model.encode(
        [
            resume_text,
            job_description
        ]
    )

    similarity_matrix = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )

    similarity_score = similarity_matrix[0][0]

    similarity_score = max(
        0.0,
        min(float(similarity_score), 1.0)
    )

    return round(
        similarity_score * 100,
        2
    ) 