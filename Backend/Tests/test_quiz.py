import pytest # type: ignore
from fastapi.testclient import TestClient
from backend.main import app # type: ignore

client = TestClient(app)

def test_generate_quiz():
    token = "mocked_token_here"
    response = client.post(
        "/quiz/generate?language=Spanish&topic=food",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "question" in response.json()[0]