import pytest
from typing import List
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

from fastapi_vo import Omit, Pick


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]


@app.get("/", response_model=List[Item])
async def read_items():
    return items


@app.get("/omit", response_model=List[Omit(Item, "description", classname="ItemName")])
async def read_items():
    return items


@app.get("/pick", response_model=List[Pick(Item, "description", classname="ItemDescription")])
async def read_items():
    return items


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
