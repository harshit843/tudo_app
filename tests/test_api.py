import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_create_task(client):
    response = client.post("/api/tasks", json={
        "title": "Test Task",
        "description": "pytest test",
        "status": "pending"
    })
    assert response.status_code == 201


def test_get_tasks(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
