from sklearn.metrics.pairwise import cosine_similarity

from app.services.semantic_matching_service import (
    get_embedding_model
)


def retrieve_relevant_chunks(
    query: str,
    chunks: list[str],
    top_k: int = 3
) -> list[str]:
    """
    Retrieve the most relevant text chunks for a query.
    """

    if not query.strip():
        return []

    if not chunks:
        return []

    if top_k <= 0:
        raise ValueError(
            "top_k must be greater than zero."
        )

    top_k = min(
        top_k,
        len(chunks)
    )

    model = get_embedding_model()

    query_embedding = model.encode(
        [query]
    )

    chunk_embeddings = model.encode(
        chunks
    )

    similarity_scores = cosine_similarity(
        query_embedding,
        chunk_embeddings
    )[0]

    ranked_indexes = similarity_scores.argsort()[::-1]

    selected_indexes = ranked_indexes[:top_k]

    return [
        chunks[index]
        for index in selected_indexes
    ]