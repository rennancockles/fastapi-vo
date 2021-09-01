def test_mixed_post(client):

    response = client.post("/mixed/", json={
        "username": "foo",
        "password": "bar",
    })
    assert response.status_code == 200
    assert response.json() == {
        "username": "foo",
        "is_admin": False,
    }
