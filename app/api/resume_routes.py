from fastapi import APIRouter
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile

from app.services.pdf_service import PDFExtractionError
from app.services.pdf_service import extract_text_from_pdf
from app.services.preprocessing_service import clean_text


router = APIRouter(
    prefix="/api/v1/resumes",
    tags=["Resumes"]
)


@router.post("/extract-text")
async def extract_resume_text(
    file: UploadFile = File(...)
):
    try:
        extracted_text = await extract_text_from_pdf(file)

    except PDFExtractionError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        ) from error

    cleaned_text = clean_text(extracted_text)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "cleaned_text": cleaned_text
    }