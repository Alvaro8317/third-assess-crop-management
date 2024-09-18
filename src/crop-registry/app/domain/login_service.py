from datetime import datetime, timezone, timedelta
import jwt
from jwt import PyJWTError
from passlib.context import CryptContext
from app.config.login import SECRET_KEY
from app.infrastructure.API.user_model import UserToCreateInDB, UserToCreate
from app.infrastructure.database.users import fake_users_db

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class LoginService:
    @staticmethod
    def create_user(user: UserToCreate):
        user_in_db = UserToCreateInDB(username=user.username,
                                      email=user.email,
                                      full_name=user.full_name,
                                      disabled=user.disabled,
                                      hashed_password=get_password_hash(user.password)
                                      )
        fake_users_db[user.username] = user_in_db
        print(fake_users_db)

    @staticmethod
    def validate_token(token: str):
        try:
            jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return True
        except PyJWTError as e:
            return False


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_user(db, username: str):
    if username in db:
        return db[username]


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(fake_db: dict, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
