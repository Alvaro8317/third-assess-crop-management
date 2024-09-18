import random
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserToCreate(UserBase):
    password: str | None = None


class UserToCreateInDB(UserBase):
    user_id: str = random.randint(3, 1000)
    hashed_password: str
