from fastapi.routing import APIRouter
from app.infraestructure.API.crop_model import CropCreateModel, CropResponseModel

crop_router = APIRouter()


@crop_router.get("/")
def test_endpoint():
    return {"message": "Hello World"}


@crop_router.post("/crops/", response_model=CropResponseModel)
def create_crop(crop_data: CropCreateModel):
    pass
    # crop_service = CropService(crop_repository)
    # use_case = CreateCropUseCase(crop_service)
    # return use_case.execute(type, variety, location, size, planting_date, harvest_date, user_id)
