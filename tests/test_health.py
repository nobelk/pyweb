import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_endpoint_content_type(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"


def test_health_endpoint_method_not_allowed(client):
    response = client.post("/health")
    assert response.status_code == 405


def test_nonexistent_endpoint(client):
    response = client.get("/nonexistent")
    assert response.status_code == 404