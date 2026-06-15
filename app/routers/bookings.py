from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import BookingCreate, BookingCreateResponse
from app.crud import create_booking, cancel_booking
from app.dependencies import get_current_user
from app.models import User

router = APIRouter(prefix="/api/v1/bookings", tags=["Bookings"])

@router.post("", response_model=BookingCreateResponse, status_code=status.HTTP_201_CREATED)
def make_booking(booking: BookingCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_booking = create_booking(db, user_id=current_user.id, movie_id=booking.movie_id, seats=booking.seats)
    return {"booking_id": new_booking.id, "status": new_booking.status.value}

@router.delete("/{id}")
def delete_booking(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    cancel_booking(db, user_id=current_user.id, booking_id=id)
    return {"message": "Booking cancelled successfully"}
