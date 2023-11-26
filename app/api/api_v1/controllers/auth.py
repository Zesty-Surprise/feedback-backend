from datetime import datetime, timedelta
from typing import Annotated

from typing import Optional
from fastapi import  Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from ....core.config import algorithm, secret_key
from ....db.mongodb import AsyncIOMotorClient, get_database
from ....repository.user import db_create_user, db_get_user_by_username, db_get_user_by_email

from ....models.user import  User
from ....models.token import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def authenticate_user(db, username: str, password: str):
    user = await db_get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt

def create_token(email):
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(data={'sub': email}, expires_delta=access_token_expires)
    return access_token

async def valid_email_from_db(email, db):
    user = await db_get_user_by_email(db, email)
    return user is not None

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db: AsyncIOMotorClient = Depends(get_database)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await db_get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def cont_create_user(user: User, db: AsyncIOMotorClient):
    user = jsonable_encoder(user)
    user = await db_create_user(user, db)
    return user