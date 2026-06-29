import pytest
import requests

@pytest.mark.smoke
@pytest.mark.regression
def test_get_movies(api_url):
    response = requests.get(f"{api_url}/movies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking_success(api_url, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"movie_id": 1, "seats": 2}
    response = requests.post(f"{api_url}/bookings", json=payload, headers=headers)
    
    assert response.status_code in [200, 201]
    data = response.json()
    assert "booking_id" in data or "id" in data

@pytest.mark.regression
def test_create_booking_unauthorized(api_url):
    payload = {"movie_id": 1, "seats": 2}
    response = requests.post(f"{api_url}/bookings", json=payload)
    
    assert response.status_code == 401
