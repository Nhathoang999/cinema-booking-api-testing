import pytest
import requests
import uuid

BASE_URL = "http://localhost:8000/api/v1"

@pytest.fixture(scope="session")
def api_url():
    return BASE_URL

@pytest.fixture(scope="session")
def test_user():
    """Generates deterministic user data for the session."""
    return {
        "username": "qa_automation_user",
        "email": f"qa_{uuid.uuid4().hex[:8]}@example.com",
        "password": "Password123!"
    }

@pytest.fixture(scope="session")
def auth_token(api_url, test_user):
    """Fixture to register and login a user, returning the JWT token."""
    # Register
    requests.post(f"{api_url}/auth/register", json=test_user)
    
    # Login
    login_payload = {"email": test_user["email"], "password": test_user["password"]}
    response = requests.post(f"{api_url}/auth/login", json=login_payload)
    if response.status_code == 200:
        return response.json().get("token")
    return None
