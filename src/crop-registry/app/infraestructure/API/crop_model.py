from pydantic import BaseModel
from datetime import date


class CropCreateModel(BaseModel):
    crop_type: str
    variety: str
    location: str
    size: int
    planting_date: date
    harvest_date: date
    user_id: int


class CropResponseModel(BaseModel):
    id: int
    crop_type: str
    variety: str
    location: str
    size: int
    planting_date: date
    harvest_date: date
    user_id: int

    class Config:
        orm_mode = True
