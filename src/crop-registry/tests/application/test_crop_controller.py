from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

crop_data = {
    "id": "f63e2818-c560-4839-8c87-7af0620c5ee6",
    "crop_type": "Lenteja",
    "variety": "1",
    "location": "Caldas",
    "size": 10,
    "planting_date": "08/24/2022",
    "harvest_date": "08/24/2023",
    "user_id": 0,
    "insert_date": "2024-09-11 20:30:00"
}


def test_get_crop():
    with patch('app.domain.services.CropService.get_crop', return_value=crop_data):
        response = client.get("/crops/?crop_id=1&user_id=1")
        assert response.status_code == 200
        assert response.json() == crop_data


def test_get_crops():
    with patch('app.domain.services.CropService.list_crops', return_value=[crop_data]):
        response = client.get("/crops/0")
        assert response.status_code == 200
        assert response.json() == [crop_data]


def test_create_crop(ftx_create_crop):
    with patch('app.domain.services.CropService.plant_crop', return_value=crop_data):
        response = client.post("/crops/", json=ftx_create_crop)
        assert response.status_code == 200
        assert response.json() == crop_data


def test_harvest_crop(ftx_harvest_crop):
    with patch('app.domain.services.CropService.harvest_crop', return_value=crop_data):
        response = client.patch("/crops/", json=ftx_harvest_crop)
        assert response.status_code == 200
        assert response.json() == crop_data


def test_delete_crop():
    with patch('app.domain.services.CropService.delete_crop', return_value=True):
        response = client.delete("/crops/?crop_id=1&user_id=1")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
