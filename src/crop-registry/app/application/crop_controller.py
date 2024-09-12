from typing import List
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.domain.services import CropService
from app.infrastructure.API.crop_model import CropCreateModel, CropResponseModel, CropHarvestModel
from app.infrastructure.repositories.cosmos_repository import CosmosCropRepository

router = APIRouter()

crop_service = CropService(CosmosCropRepository())


@router.get("/crops/", response_model=CropResponseModel, status_code=status.HTTP_200_OK)
def get_crop(crop_id: str, user_id: int):
    crop = crop_service.get_crop(crop_id, user_id)
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")
    return JSONResponse(crop)


@router.get("/crops/{user_id}", response_model=List[CropResponseModel])
def get_crops(user_id: int):
    crops = crop_service.list_crops(user_id)
    return crops


@router.post("/crops/", response_model=CropResponseModel)
def create_crop(crop_data: CropCreateModel):
    return crop_service.plant_crop(crop_data.model_dump())


@router.patch("/crops/", response_model=CropResponseModel)
def harvest_crop(crop_data: CropHarvestModel):
    result = crop_service.harvest_crop(crop_data.model_dump())
    if not result:
        raise HTTPException(status_code=404, detail="Crop not found")
    return result


@router.delete("/crops/", response_model=dict)
def delete_crop(crop_id: str, user_id: int):
    result = crop_service.delete_crop(crop_id, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Crop not found")
    return JSONResponse({"status": "ok"})
