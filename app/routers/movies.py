from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import MovieResponse
from app.crud import get_movies, get_movie_by_id

router = APIRouter(prefix="/api/v1/movies", tags=["Movies"])

@router.get("", response_model=List[MovieResponse])
def read_movies(db: Session = Depends(get_db)):
    return get_movies(db)

@router.get("/{id}", response_model=MovieResponse)
def read_movie(id: int, db: Session = Depends(get_db)):
    return get_movie_by_id(db, id)
