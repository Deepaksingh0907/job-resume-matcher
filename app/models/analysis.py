from datetime import datetime
from datetime import timezone

from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import JSON
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    resume_filename: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    extracted_text: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    cleaned_resume: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    job_description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    tfidf_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    semantic_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    skill_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    overall_score: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    resume_skills: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False
    )

    job_skills: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False
    )

    matched_skills: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False
    )

    missing_skills: Mapped[list[str]] = mapped_column(
        JSON,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )