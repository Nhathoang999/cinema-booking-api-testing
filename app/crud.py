from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models import User, Movie, Booking, BookingStatus
from app.schemas import UserCreate
from app.security import get_password_hash
from datetime import datetime, timezone

def create_user(db: Session, user: UserCreate):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error_code": "EMAIL_EXISTS", "message": "Email already exists"}
        )
    
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_movies(db: Session):
    return db.query(Movie).all()

def get_movie_by_id(db: Session, movie_id: int):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error_code": "MOVIE_NOT_FOUND", "message": "Movie not found"}
        )
    return movie

def create_booking(db: Session, user_id: int, movie_id: int, seats: int):
    movie = get_movie_by_id(db, movie_id)
    if movie.available_seats < seats:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error_code": "NOT_ENOUGH_SEATS", "message": "Not enough seats available"}
        )
    
    # Deduct seats
    movie.available_seats -= seats
    
    booking = Booking(user_id=user_id, movie_id=movie_id, seats=seats, status=BookingStatus.ACTIVE)
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def cancel_booking(db: Session, user_id: int, booking_id: int):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error_code": "BOOKING_NOT_FOUND", "message": "Booking not found"}
        )
    
    if booking.user_id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"error_code": "FORBIDDEN", "message": "Forbidden: You do not own this booking"}
        )
    
    if booking.status == BookingStatus.CANCELLED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error_code": "BOOKING_ALREADY_CANCELLED", "message": "Booking already cancelled"}
        )
    
    # Restore seats
    movie = booking.movie
    movie.available_seats += booking.seats
    
    booking.status = BookingStatus.CANCELLED
    booking.cancelled_at = datetime.now(timezone.utc)
    
    db.commit()
    return booking

def get_user_bookings(db: Session, user_id: int, status_filter: str = None, limit: int = 100):
    query = db.query(Booking).filter(Booking.user_id == user_id)
    if status_filter:
        query = query.filter(Booking.status == status_filter.upper())
    return query.limit(limit).all()
