from fastapi.testclient import TestClient
from backend.main import app # type: ignore

client = TestClient(app)

def test_mentor_ask():
    client.post("/auth/register", json={
        "username": "mentoruser",
        "email": "mentor@example.com",
        "password": "pass123"
    })
    token = client.post("/auth/login", data={
        "username": "mentor@example.com",
        "password": "pass123"
    }).json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    
    response = client.post("/mentor/ask", json={
        "language": "French",
        "query": "How do I say 'Good morning'?"
    }, headers=headers)
    
    assert response.status_code == 200
    assert "response" in response.json()
    
    