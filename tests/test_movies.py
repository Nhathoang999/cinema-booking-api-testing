from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_movies():
    response = client.get("/api/v1/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_movie_not_found():
    response = client.get("/api/v1/movies/9999")
    assert response.status_code == 404
    assert response.json()["error_code"] == "MOVIE_NOT_FOUND"
