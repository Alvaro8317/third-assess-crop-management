from datetime import timedelta
from typing_extensions import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.infrastructure.API.user_model import UserToCreate
from app.infrastructure.API.token_model import Token
from app.domain.login_service import authenticate_user, create_access_token, LoginService
from app.infrastructure.database.users import fake_users_db

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
login_service = LoginService()
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@router.post("/create-user",
             tags=["User Management"],
             summary="Create a new user",
             description="This endpoint allows for the creation of a new user in the system.",
             status_code=status.HTTP_201_CREATED)
async def create_user(user: UserToCreate):
    login_service.create_user(user)
    return {"message": "User created successfully"}


@router.post("/token",
             tags=["Authentication"],
             response_model=Token,
             summary="Obtain access token",
             description="Login with username and password to receive an access token for future requests.",
             status_code=status.HTTP_200_OK)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return Token(access_token=access_token, token_type="bearer")
