from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
    resume_text: str,
    job_description: str
) -> float:
    if not resume_text.strip():
        return 0.0

    if not job_description.strip():
        return 0.0

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    similarity_matrix = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    similarity_score = similarity_matrix[0][0]

    return round(
        float(similarity_score) * 100,
        2
    ) 