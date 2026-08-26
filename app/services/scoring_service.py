def calculate_overall_score(
    tfidf_score: float,
    semantic_score: float,
    skill_score: float
) -> float:
    overall_score = (
        (tfidf_score * 0.20)
        + (semantic_score * 0.40)
        + (skill_score * 0.40)
    )

    return round(
        overall_score,
        2
    )