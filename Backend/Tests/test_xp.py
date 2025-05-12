from fastapi.testclient import TestClient
from backend.main import app # type: ignore

client = TestClient(app)

def test_xp_gain_and_check():
    client.post("/auth/register", json={
        "username": "xpuser",
        "email": "xp@example.com",
        "password": "password"
    })
    token = client.post("/auth/login", data={
        "username": "xp@example.com",
        "password": "password"
    }).json()["access_token"]
    
    headers = {"Authorization": f"Bearer {token}"}
    
    gain = client.post("/xp/gain?points=30", headers=headers)
    assert gain.status_code == 200
    assert gain.json()["points"] >= 30
    
    check = client.get("/xp/", headers=headers)
    assert check.status_code == 200
    assert check.json()["points"] >= 30