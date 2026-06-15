from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional, List
from datetime import datetime
from app.models import BookingStatus

# --- Error Schema ---
class ErrorResponse(BaseModel):
    error_code: str
    message: str

# --- User Schemas ---
class UserCreate(BaseModel):
    username: str = Field(..., max_length=150)
    email: EmailStr
    password: str = Field(..., min_length=6)

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "username": "johndoe",
            "email": "johndoe@example.com",
            "password": "Password123!"
        }
    })

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "email": "johndoe@example.com",
            "password": "Password123!"
        }
    })

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    token: str
    token_type: str = "bearer"

# --- Movie Schemas ---
class MovieResponse(BaseModel):
    id: int
    title: str
    genre: str
    duration: int
    release_date: str
    total_seats: int
    available_seats: int

    model_config = ConfigDict(from_attributes=True)

# --- Booking Schemas ---
class BookingCreate(BaseModel):
    movie_id: int
    seats: int = Field(..., gt=0)

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "movie_id": 1,
            "seats": 2
        }
    })

class BookingResponse(BaseModel):
    id: int
    user_id: int
    movie_id: int
    seats: int
    status: BookingStatus
    created_at: datetime
    updated_at: datetime
    cancelled_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

class BookingCreateResponse(BaseModel):
    booking_id: int
    status: str
