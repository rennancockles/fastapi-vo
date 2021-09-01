import pytest


@pytest.fixture(scope="module")
def user_omit_list(user_list):
    list_ = [u.copy() for u in user_list]
    for u in list_:
        u.pop("password")
    return list_


def test_omit_list(client, user_omit_list):
    print(user_omit_list)
    response = client.get("/omit/")
    assert response.status_code == 200
    assert response.json() == user_omit_list


def test_omit_get(client, user_omit_list):
    print(user_omit_list)
    response = client.get("/omit/1")
    assert response.status_code == 200
    assert response.json() == user_omit_list[0]


def test_omit_post(client, user_omit_list):
    response = client.post("/omit/", json=user_omit_list[0])
    assert response.status_code == 200
    assert response.json() == user_omit_list[0]
