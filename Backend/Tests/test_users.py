import pytest # type: ignore
from fastapi.testclient import TestClient
from backend.main import app # type: ignore

client = TestClient(app)

def test_register_user():
    response = client.post("/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "securepassword"  
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"
    
def test_login_user():
    response = client.post("/auth/login", data={
        "username": "test@example.com",
        "password": "securepassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
