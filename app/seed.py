from app.database import SessionLocal, engine, Base
from app.models import Movie
from sqlalchemy.orm import Session

def seed_data(db: Session):
    movies = [
        {"title": "Avengers Endgame", "genre": "Action/Sci-Fi", "duration": 181, "release_date": "2019-04-26", "total_seats": 100, "available_seats": 100},
        {"title": "Interstellar", "genre": "Sci-Fi/Drama", "duration": 169, "release_date": "2014-11-07", "total_seats": 50, "available_seats": 50},
        {"title": "Oppenheimer", "genre": "Biography/Drama", "duration": 180, "release_date": "2023-07-21", "total_seats": 200, "available_seats": 200},
        {"title": "Joker", "genre": "Crime/Drama", "duration": 122, "release_date": "2019-10-04", "total_seats": 80, "available_seats": 80},
        {"title": "Dune Part Two", "genre": "Sci-Fi/Adventure", "duration": 166, "release_date": "2024-03-01", "total_seats": 150, "available_seats": 150},
    ]

    for movie_data in movies:
        existing = db.query(Movie).filter(Movie.title == movie_data["title"]).first()
        if not existing:
            movie = Movie(**movie_data)
            db.add(movie)
    
    db.commit()
    print("Database seeded successfully with initial movies!")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        seed_data(db)
    finally:
        db.close()
