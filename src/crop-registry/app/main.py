from fastapi import FastAPI
from app.infraestructure.API.crop_controller import crop_router

app = FastAPI()
app.include_router(crop_router)
