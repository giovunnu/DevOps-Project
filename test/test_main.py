from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_helloworld():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
