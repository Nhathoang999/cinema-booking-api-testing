import pytest
import requests

BASE_URL = "http://localhost:8000/api/v1"

@pytest.fixture(scope="session")
def api_url():
    return BASE_URL

@pytest.fixture(scope="session")
def auth_token(api_url):
    """Fixture to register and login a user, returning the JWT token."""
    # Since email needs to be unique, we can generate a random one or use a test one.
    import uuid
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123!"
    
    # Register
    requests.post(f"{api_url}/auth/register", json={"email": email, "password": password})
    
    # Login
    response = requests.post(f"{api_url}/auth/login", json={"email": email, "password": password})
    if response.status_code == 200:
        return response.json().get("access_token")
    return None
