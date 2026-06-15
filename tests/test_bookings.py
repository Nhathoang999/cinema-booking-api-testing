from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_booking_unauthorized():
    response = client.post("/api/v1/bookings", json={
        "movie_id": 1,
        "seats": 2
    })
    assert response.status_code == 401
