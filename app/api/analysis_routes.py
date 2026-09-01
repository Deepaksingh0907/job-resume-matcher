from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.database import get_db
from app.models import Analysis
from app.models import User
from app.schemas.analysis_history_schema import (
    AnalysisHistoryResponse
)


router = APIRouter(
    prefix="/api/v1/analyses",
    tags=["Analysis History"]
)


@router.get(
    "/history",
    response_model=list[AnalysisHistoryResponse]
)
def get_analysis_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = (
        select(Analysis)
        .where(
            Analysis.user_id == current_user.id
        )
        .order_by(
            Analysis.created_at.desc()
        )
    )

    analyses = db.scalars(query).all()

    return analyses