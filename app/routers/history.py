from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.schemas import BookingResponse
from app.crud import get_user_bookings
from app.dependencies import get_current_user
from app.models import User

router = APIRouter(prefix="/api/v1/user", tags=["History"])

@router.get("/bookings", response_model=List[BookingResponse])
def get_history(
    status: Optional[str] = Query(None, description="Filter by ACTIVE or CANCELLED"),
    limit: int = Query(100, le=1000, description="Max number of records"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_bookings(db, user_id=current_user.id, status_filter=status, limit=limit)
