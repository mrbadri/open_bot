"""Bot user management routes for admin API."""

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from features.users.models import BotUser
from features.users.repository import BotUserRepository
from features.users.schemas import BotUserResponse
from common.pagination import PaginationParams, PaginatedResponse

router = APIRouter()


@router.get("/", response_model=PaginatedResponse[BotUserResponse])
async def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
):
    """List all bot users with pagination."""
    pagination = PaginationParams(page=page, page_size=page_size)
    
    # Get total count
    total = db.query(BotUser).count()
    
    # Get paginated users
    users = (
        db.query(BotUser)
        .order_by(BotUser.created_at.desc())
        .offset(pagination.offset)
        .limit(pagination.limit)
        .all()
    )
    
    return PaginatedResponse.create(
        items=[BotUserResponse.model_validate(user) for user in users],
        total=total,
        page=pagination.page,
        page_size=pagination.page_size,
    )


@router.get("/{user_id}", response_model=BotUserResponse)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    """Get bot user by ID."""
    user = db.query(BotUser).filter(BotUser.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return BotUserResponse.model_validate(user)


@router.get("/bale/{bale_user_id}", response_model=BotUserResponse)
async def get_user_by_bale_id(
    bale_user_id: int,
    db: Session = Depends(get_db),
):
    """Get bot user by Bale user ID."""
    repository = BotUserRepository(db)
    user = repository.get_by_bale_user_id(bale_user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return BotUserResponse.model_validate(user)
