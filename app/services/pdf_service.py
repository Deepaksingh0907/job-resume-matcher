import pymupdf

from fastapi import UploadFile


class PDFExtractionError(Exception):
    pass


async def extract_text_from_pdf(file: UploadFile) -> str:
    if not file.filename:
        raise PDFExtractionError("Filename is missing.")

    if not file.filename.lower().endswith(".pdf"):
        raise PDFExtractionError("Only PDF files are allowed.")

    file_bytes = await file.read()

    if not file_bytes:
        raise PDFExtractionError("The uploaded file is empty.")

    try:
        with pymupdf.open(
            stream=file_bytes,
            filetype="pdf"
        ) as document:
            extracted_text = "\n".join(
                page.get_text()
                for page in document
            )

    except Exception as error:
        raise PDFExtractionError(
            "The uploaded file is not a valid PDF."
        ) from error

    if not extracted_text.strip():
        raise PDFExtractionError(
            "No readable text was found in the PDF."
        )

    return extracted_text.strip()