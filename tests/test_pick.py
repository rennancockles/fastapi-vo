import pytest


@pytest.fixture(scope="module")
def user_pick_list(user_list):
    return [{"password": u.get("password")} for u in user_list]


def test_pick_list(client, user_pick_list):
    print(user_pick_list)
    response = client.get("/pick/")
    assert response.status_code == 200
    assert response.json() == user_pick_list


def test_pick_get(client, user_pick_list):
    print(user_pick_list)
    response = client.get("/pick/1")
    assert response.status_code == 200
    assert response.json() == user_pick_list[0]


def test_pick_post(client, user_pick_list):
    response = client.post("/pick/", json=user_pick_list[0])
    assert response.status_code == 200
    assert response.json() == user_pick_list[0]
