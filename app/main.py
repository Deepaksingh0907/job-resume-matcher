from fastapi import FastAPI

from app.api.match_routes import router as match_router
from app.api.resume_routes import router as resume_router


app = FastAPI(
    title="Job Resume Matcher",
    description="Match resumes with job descriptions using NLP and machine learning.",
    version="0.1.0",
)


app.include_router(resume_router)
app.include_router(match_router)


@app.get("/")
def read_root():
    return {
        "message": "Job Resume Matcher API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }