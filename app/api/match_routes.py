from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import Form
from fastapi import HTTPException
from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.database import get_db
from app.models import User
from app.models import Analysis
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
    job_description: str = Form(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
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

    analysis = Analysis(
        user_id=current_user.id,
        resume_filename=file.filename or "unknown.pdf",
        extracted_text=extracted_text,
        cleaned_resume=cleaned_resume,
        job_description=job_description,
        tfidf_score=tfidf_score,
        semantic_score=semantic_score,
        skill_score=skill_analysis["skill_score"],
        overall_score=overall_score,
        resume_skills=skill_analysis["resume_skills"],
        job_skills=skill_analysis["job_skills"],
        matched_skills=skill_analysis["matched_skills"],
        missing_skills=skill_analysis["missing_skills"]
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

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