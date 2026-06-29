import requests
import uuid

def test_register_success(api_url):
    email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    payload = {"email": email, "password": "Password123!"}
    response = requests.post(f"{api_url}/auth/register", json=payload)
    
    # Allow 201 or 200 depending on actual API implementation
    assert response.status_code in [200, 201]
    data = response.json()
    assert "email" in data

def test_register_duplicate_email(api_url):
    email = f"user_{uuid.uuid4().hex[:8]}@example.com"
    payload = {"email": email, "password": "Password123!"}
    requests.post(f"{api_url}/auth/register", json=payload)
    
    # Try again
    response = requests.post(f"{api_url}/auth/register", json=payload)
    assert response.status_code == 400  # or 409

def test_login_success(api_url, auth_token):
    # auth_token fixture handles registration and login behind the scenes
    # If it returns a token, login was successful.
    assert auth_token is not None
    assert len(auth_token) > 0
