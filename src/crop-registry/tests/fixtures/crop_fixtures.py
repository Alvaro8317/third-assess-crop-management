import pytest
import uuid


@pytest.fixture(scope="function")
def ftx_create_crop():
    return {
        "crop_type": "Arroz",
        "variety": "1",
        "location": "Caldas",
        "size": 10,
        "planting_date": "2019-08-24",
        "harvest_date": "2025-08-24",
        "user_id": 0
    }


@pytest.fixture(scope="function")
def ftx_harvest_crop():
    return {
        "crop_id": str(uuid.uuid4()),
        "planting_date": "2022-08-24",
        "harvest_date": "2023-08-24",
        "user_id": 0
    }
