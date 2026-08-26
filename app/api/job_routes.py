from fastapi import APIRouter

from app.schemas.job_schema import JobDescriptionRequest
from app.services.preprocessing_service import normalize_text


router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.post("/description")
def submit_job_description(
    request: JobDescriptionRequest,
) -> dict[str, str]:
    """Validate and normalize a submitted job description."""
    cleaned_description = normalize_text(
        request.job_description
    )

    return {
        "message": "Job description processed successfully",
        "original_description": request.job_description,
        "cleaned_description": cleaned_description,
    }