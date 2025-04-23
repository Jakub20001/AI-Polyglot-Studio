import pytest # type: ignore
from fastapi.testclient import TestClient
from backend.main import app # type: ignore

client = TestClient(app)

def test_generate_dialogue():
    token = "mocked_token_here"
    response = client.post(
        "/dialogue/generate",
        json={"topic": "introductions", "level": "beginner"},
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert "dialogue" in response.json()