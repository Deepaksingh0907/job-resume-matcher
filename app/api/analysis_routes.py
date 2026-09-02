from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi import status

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.schemas.analysis_history_schema import (
    AnalysisHistoryListResponse,
    AnalysisHistoryResponse
)    
from app.api.dependencies import get_current_user
from app.database import get_db
from app.models import Analysis
from app.models import User



router = APIRouter(
    prefix="/api/v1/analyses",
    tags=["Analysis History"]
)


@router.get(
    "/history",
    response_model=AnalysisHistoryListResponse
)
def get_analysis_history(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    total = db.scalar(
        select(func.count(Analysis.id)).where(
            Analysis.user_id == current_user.id
        )
    )

    query = (
        select(Analysis)
        .where(
            Analysis.user_id == current_user.id
        )
        .order_by(
            Analysis.created_at.desc()
        )
        .offset(skip)
        .limit(limit)
    )

    analyses = db.scalars(query).all()

    return {
        "total": total or 0, 
        "skip": skip,
        "limit": limit,
        "items": analyses
    }


@router.get(
    "/{analysis_id}",
    response_model=AnalysisHistoryResponse
)
def get_analysis_by_id(
    analysis_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    analysis = db.scalar(
        select(Analysis).where(
            Analysis.id == analysis_id,
            Analysis.user_id == current_user.id
        )
    )

    if analysis is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Analysis not found"
        )

    return analysis