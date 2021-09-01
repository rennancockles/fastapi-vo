from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi_vo import Omit, Pick


app = FastAPI()


class User(BaseModel):
    username: str
    password: str
    is_active: bool
    is_admin: Optional[bool] = False


NoPass = Omit(User, "password", classname="NoPass")
OnlyPass = Pick(User, "password", classname="OnlyPass")


users = [
    {
        "username": "johndoe",
        "password": "secret",
        "is_active": True,
        "is_admin": False,
    },
    {
        "username": "janedoe",
        "password": "secret123",
        "is_active": True,
        "is_admin": True,
    },
]


# Default
@app.get("/", response_model=List[User])
async def list_users():
    return users


@app.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    if 0 < user_id <= len(users):
        return users[user_id - 1]
    return None


# Omit
@app.get("/omit/", response_model=List[NoPass])
async def list_omit_users():
    return users


@app.get("/omit/{user_id}", response_model=NoPass)
async def get_omit_user(user_id: int):
    if 0 < user_id <= len(users):
        return users[user_id - 1]
    return None


# Pick
@app.get("/pick/", response_model=List[OnlyPass])
async def list_pick_users():
    return users


@app.get("/pick/{user_id}", response_model=OnlyPass)
async def get_pick_user(user_id: int):
    if 0 < user_id <= len(users):
        return users[user_id - 1]
    return None
