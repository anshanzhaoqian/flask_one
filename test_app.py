import pytest
from app import app

@pytest.fixture
def client():
    """Configures the Flask app for testing."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Tests the root health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"status": "healthy", "message": "Flask API is running"}

def test_multiply_endpoint(client):
    """Tests the math multiplication endpoint."""
    response = client.get("/multiply/3/5")
    assert response.status_code == 200
    assert response.json == {"result": 15}
