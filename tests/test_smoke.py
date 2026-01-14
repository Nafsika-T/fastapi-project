from fastapi.testclient import TestClient
from app.main import app

def test_app_starts(client):
    r= client.get("/docs")
    assert r.status_code == 200