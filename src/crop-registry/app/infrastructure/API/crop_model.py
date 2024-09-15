from pydantic import BaseModel, field_serializer
from datetime import date


class CropBaseModel(BaseModel):
    planting_date: date
    harvest_date: date
    user_id: int

    @field_serializer('planting_date')
    def serialize_planting_date(self, date_to_serialize: date):
        return date_to_serialize.strftime('%m/%d/%Y')

    @field_serializer('harvest_date')
    def serialize_harvest_date(self, date_to_serialize: date):
        return date_to_serialize.strftime('%m/%d/%Y')


class CropCreateModel(CropBaseModel):
    crop_type: str
    variety: str
    location: str
    size: int


class CropHarvestModel(CropBaseModel):
    crop_id: str


class CropResponseModel(BaseModel):
    id: str
    crop_type: str
    variety: str
    location: str
    size: int
    planting_date: str
    harvest_date: str
    user_id: int
    insert_date: str

    class ConfigDict:
        from_attributes = True
