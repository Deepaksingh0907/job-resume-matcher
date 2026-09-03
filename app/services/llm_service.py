import json
from json import JSONDecodeError

import httpx

from app.core.config import settings
from app.services.chunking_service import create_chunks
from app.services.retrieval_service import (
    retrieve_relevant_chunks
)


class LLMServiceError(Exception):
    pass


def _parse_llm_response(content: str) -> dict:
    content = content.strip()

    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    try:
        result = json.loads(content)

    except JSONDecodeError as error:
        raise LLMServiceError(
            "The LLM returned invalid JSON."
        ) from error

    return {
        "summary": str(
            result.get(
                "summary",
                "No summary was generated."
            )
        ),
        "strengths": result.get(
            "strengths",
            []
        ),
        "recommendations": result.get(
            "recommendations",
            []
        ),
        "interview_questions": result.get(
            "interview_questions",
            []
        )
    }


async def generate_match_insights(
    resume_text: str,
    job_description: str,
    overall_score: float,
    tfidf_score: float,
    semantic_score: float,
    skill_analysis: dict
) -> dict:
    if not settings.openrouter_api_key:
        raise LLMServiceError(
            "OPENROUTER_API_KEY is not configured."
        )

    try:
        resume_chunks = create_chunks(
            resume_text
        )

        job_chunks = create_chunks(
            job_description
        )

        retrieval_query = (
            "What resume experience, projects, and skills "
            "are most relevant to the job requirements?"
        )

        relevant_resume_chunks = retrieve_relevant_chunks(
            query=retrieval_query,
            chunks=resume_chunks,
            top_k=4
        )

        relevant_job_chunks = retrieve_relevant_chunks(
            query=retrieval_query,
            chunks=job_chunks,
            top_k=4
        )

    except Exception as error:
        raise LLMServiceError(
            "RAG retrieval failed."
        ) from error


    resume_context = "\n\n".join(
        relevant_resume_chunks
    )

    job_context = "\n\n".join(
        relevant_job_chunks
    )


    prompt = f"""
You are a professional resume-analysis assistant.

Analyze the resume against the job description.

Use only the retrieved context below.
Do not invent skills, experience, or qualifications.

Return valid JSON only in this format:

{{
    "summary": "short match explanation",
    "strengths": [
        "strength 1",
        "strength 2"
    ],
    "recommendations": [
        "recommendation 1",
        "recommendation 2"
    ],
    "interview_questions": [
        "question 1",
        "question 2"
    ]
}}

Retrieved Resume Context:
{resume_context}

Retrieved Job Description Context:
{job_context}

Existing Scores:
Overall score: {overall_score}
TF-IDF score: {tfidf_score}
Semantic score: {semantic_score}

Skill Analysis:
{json.dumps(skill_analysis, indent=2)}
"""


    payload = {
        "model": settings.llm_model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You analyze resumes accurately "
                    "using retrieved evidence and return JSON."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2
    }


    headers = {
        "Authorization": (
            f"Bearer {settings.openrouter_api_key}"
        ),
        "Content-Type": "application/json"
    }


    endpoint = (
        f"{settings.openrouter_base_url.rstrip('/')}"
        "/chat/completions"
    )


    try:
        async with httpx.AsyncClient(
            timeout=settings.llm_timeout_seconds
        ) as client:
            response = await client.post(
                endpoint,
                headers=headers,
                json=payload
            )

        response.raise_for_status()

        response_data = response.json()

        content = response_data[
            "choices"
        ][0]["message"]["content"]

        return _parse_llm_response(content)

    except httpx.HTTPError as error:
        raise LLMServiceError(
            "The LLM request failed."
        ) from error

    except (KeyError, IndexError, TypeError) as error:
        raise LLMServiceError(
            "The LLM returned an unexpected response."
        ) from error