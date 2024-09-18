from typing import List
from typing_extensions import Annotated
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from app.domain.crop_service import CropService
from app.domain.login_service import LoginService
from app.infrastructure.API.crop_model import CropCreateModel, CropResponseModel, CropHarvestModel
from app.infrastructure.repositories.cosmos_repository import CosmosCropRepository
from app.application.login_controller import oauth2_scheme

router = APIRouter()
crop_service = CropService(CosmosCropRepository())
login_service = LoginService()


@router.get("/crops/",
            response_model=CropResponseModel,
            status_code=status.HTTP_200_OK,
            tags=["Crops"],
            summary="Get crop by ID",
            description="Returns the information of a specific crop based on its `crop_id` "
                        "and the associated `user_id`.")
def get_crop(token: Annotated[str, Depends(oauth2_scheme)], crop_id: str, user_id: int):
    is_valid_token: bool = login_service.validate_token(token)
    if not is_valid_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    crop = crop_service.get_crop(crop_id, user_id)
    if not crop:
        raise HTTPException(status_code=404, detail="Crop not found")
    return JSONResponse(crop, status_code=status.HTTP_200_OK)


@router.get("/crops/{user_id}",
            response_model=List[CropResponseModel],
            tags=["Crops"],
            summary="List all user's crops",
            description="Returns a list of all crops associated with a specific `user_id`.")
def get_crops(token: Annotated[str, Depends(oauth2_scheme)], user_id: int):
    is_valid_token: bool = login_service.validate_token(token)
    if not is_valid_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    crops = crop_service.list_crops(user_id)
    return crops


@router.post("/crops/",
             response_model=CropResponseModel,
             tags=["Crops"],
             summary="Create a new crop",
             description="Creates a new crop based on the provided data and associates it with a user.")
def create_crop(token: Annotated[str, Depends(oauth2_scheme)], crop_data: CropCreateModel):
    is_valid_token: bool = login_service.validate_token(token)
    if not is_valid_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return crop_service.plant_crop(crop_data.model_dump())


@router.patch("/crops/",
              response_model=CropResponseModel,
              tags=["Crops"],
              summary="Harvest a crop",
              description="Updates the status of an existing crop to mark it as harvested. "
                          "If the crop is not found, returns a 404 error.")
def harvest_crop(token: Annotated[str, Depends(oauth2_scheme)], crop_data: CropHarvestModel):
    is_valid_token: bool = login_service.validate_token(token)
    if not is_valid_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    result = crop_service.harvest_crop(crop_data.model_dump())
    if not result:
        raise HTTPException(status_code=404, detail="Crop not found")
    return result


@router.delete("/crops/",
               response_model=dict,
               tags=["Crops"],
               summary="Delete a crop",
               description="Deletes a crop based on its `crop_id` and `user_id`. "
                           "If the crop is not found, returns a 404 error.")
def delete_crop(token: Annotated[str, Depends(oauth2_scheme)], crop_id: str, user_id: int):
    is_valid_token: bool = login_service.validate_token(token)
    if not is_valid_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    result = crop_service.delete_crop(crop_id, user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Crop not found")
    return JSONResponse({"status": "ok"})
