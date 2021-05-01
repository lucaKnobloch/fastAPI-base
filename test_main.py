import datetime

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_status_main():
    response = client.get("/status")
    assert response.status_code == 200
    time = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
    assert response.json() == {"status": "UP", "time": time}


