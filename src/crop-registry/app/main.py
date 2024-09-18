from fastapi import FastAPI
from app.application.crop_controller import router as crop_router
from app.application.login_controller import router as login_router

app = FastAPI()
app.include_router(crop_router)
app.include_router(login_router)
