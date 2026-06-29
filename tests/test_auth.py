import pytest
import requests
import uuid

@pytest.mark.smoke
@pytest.mark.regression
def test_register_success(api_url):
    email = f"qa_{uuid.uuid4().hex[:8]}@example.com"
    payload = {"username": "new_qa_user", "email": email, "password": "Password123!"}
    response = requests.post(f"{api_url}/auth/register", json=payload)
    
    assert response.status_code in [200, 201]
    data = response.json()
    # Assuming standard success response
    assert "message" in data or "email" in data

@pytest.mark.regression
def test_register_duplicate_email(api_url):
    email = f"qa_{uuid.uuid4().hex[:8]}@example.com"
    payload = {"username": "dup_user", "email": email, "password": "Password123!"}
    requests.post(f"{api_url}/auth/register", json=payload)
    
    # Try again
    response = requests.post(f"{api_url}/auth/register", json=payload)
    assert response.status_code == 400
    assert response.json().get("error_code") == "EMAIL_EXISTS" or "already exists" in response.text

@pytest.mark.smoke
@pytest.mark.regression
def test_login_success(api_url, auth_token):
    assert auth_token is not None
    assert len(auth_token) > 0
