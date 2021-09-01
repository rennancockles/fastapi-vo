import pytest
from fastapi.testclient import TestClient

from .apptest import app, users


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def user_list():
    return users
