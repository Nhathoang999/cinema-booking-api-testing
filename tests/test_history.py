from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_history_unauthorized():
    response = client.get("/api/v1/user/bookings")
    assert response.status_code == 401
