from fastapi import APIRouter
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import UploadFile

from app.schemas.analysis_schema import AnalysisResponse
from app.services.matching_service import calculate_similarity
from app.services.pdf_service import PDFExtractionError
from app.services.pdf_service import extract_text_from_pdf
from app.services.preprocessing_service import clean_text
from app.services.scoring_service import calculate_overall_score
from app.services.semantic_matching_service import (
    calculate_semantic_similarity
)
from app.services.skill_matching_service import compare_skills


router = APIRouter(
    prefix="/api/v1/matches",
    tags=["Matching"]
)


@router.post(
    "/analyze",
    response_model=AnalysisResponse
)
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    try:
        extracted_text = await extract_text_from_pdf(file)

    except PDFExtractionError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    cleaned_resume = clean_text(extracted_text)

    cleaned_job_description = clean_text(
        job_description
    )

    tfidf_score = calculate_similarity(
        cleaned_resume,
        cleaned_job_description
    )

    semantic_score = calculate_semantic_similarity(
        cleaned_resume,
        cleaned_job_description
    )

    skill_analysis = compare_skills(
        cleaned_resume,
        cleaned_job_description
    )

    overall_score = calculate_overall_score(
        tfidf_score,
        semantic_score,
        skill_analysis["skill_score"]
    )

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "cleaned_resume": cleaned_resume,
        "cleaned_job_description": cleaned_job_description,
        "tfidf_score": tfidf_score,
        "semantic_score": semantic_score,
        "skill_analysis": skill_analysis,
        "overall_score": overall_score
    }