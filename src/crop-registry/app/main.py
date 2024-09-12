from fastapi import FastAPI
from app.application.crop_controller import router as crop_router

app = FastAPI()
app.include_router(crop_router)
