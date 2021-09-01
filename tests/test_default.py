def test_default_list(client, user_list):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == user_list


def test_default_get(client, user_list):
    response = client.get("/1")
    assert response.status_code == 200
    assert response.json() == user_list[0]
