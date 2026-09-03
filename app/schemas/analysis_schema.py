from pydantic import BaseModel


class SkillAnalysisResponse(BaseModel):
    resume_skills: list[str]
    job_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    skill_score: float


class LLMInsightsResponse(BaseModel):
    summary: str
    strengths: list[str]
    recommendations: list[str]
    interview_questions: list[str]


class AnalysisResponse(BaseModel):
    filename: str
    extracted_text: str
    cleaned_resume: str
    cleaned_job_description: str

    tfidf_score: float
    semantic_score: float

    skill_analysis: SkillAnalysisResponse

    overall_score: float

    llm_insights: LLMInsightsResponse | None = None