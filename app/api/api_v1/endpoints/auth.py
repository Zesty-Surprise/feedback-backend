from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ....core.config import access_token_expire_minutes
from ....db.mongodb import AsyncIOMotorClient, get_database
from ..controllers.auth import authenticate_user, create_access_token, get_current_user, cont_create_user

from ....models.token import Token
from ....models.user import User

router = APIRouter(tags=["Auth"])

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncIOMotorClient = Depends(get_database), 
):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)]
):
    user_data = await current_user
    return user_data


@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_user)]
):
    current_user_instance = await current_user
    return [{"item_id": "Foo", "owner": current_user_instance["username"]}]

@router.post("/users", response_model=User)
async def add_user(user: User, db: AsyncIOMotorClient = Depends(get_database)):
    user = await cont_create_user(user, db)    
    if user:
        return user
    return HTTPException(404, f"user failed to create")