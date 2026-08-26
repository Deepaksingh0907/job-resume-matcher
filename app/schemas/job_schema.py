from pydantic import BaseModel, Field


class JobDescriptionRequest(BaseModel):
    """Request body used when submitting a job description."""

    job_description: str = Field(
        ...,
        min_length=20,
        max_length=10_000,
        description="The job description that will be compared with a resume.",
    )