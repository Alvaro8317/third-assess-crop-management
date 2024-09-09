from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

client = TestClient(app)


def setup_module(module):
    Base.metadata.create_all(bind=engine)


def teardown_module(module):
    Base.metadata.drop_all(bind=engine)


def test_create_crop():
    response = client.post(
        "/crops/",
        json={
            "type": "Vegetable",
            "variety": "Tomato",
            "location": "Farm A",
            "size": 100,
            "planting_date": "2024-01-01",
            "harvest_date": "2024-06-01",
            "user_id": 1,
        },
    )
    assert response.status_code == 200
    assert response.json()["type"] == "Vegetable"


def test_read_crop():
    response = client.get("/crops/1")
    assert response.status_code == 200
    assert response.json()["type"] == "Vegetable"


def test_update_crop():
    response = client.put(
        "/crops/1",
        json={
            "type": "Fruit",
            "variety": "Apple",
            "location": "Farm B",
            "size": 150,
            "planting_date": "2024-02-01",
            "harvest_date": "2024-07-01",
            "user_id": 2,
        },
    )
    assert response.status_code == 200
    assert response.json()["type"] == "Fruit"


def test_delete_crop():
    response = client.delete("/crops/1")
    assert response.status_code == 200
    assert response.json()["type"] == "Fruit"
