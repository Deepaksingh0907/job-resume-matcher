from datetime import datetime

from pydantic import BaseModel


class AnalysisHistoryResponse(BaseModel):
    id: int
    resume_filename: str
    tfidf_score: float
    semantic_score: float
    skill_score: float
    overall_score: float
    matched_skills: list[str]
    missing_skills: list[str]
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class AnalysisHistoryListResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: list[AnalysisHistoryResponse]