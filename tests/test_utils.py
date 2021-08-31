def test_default(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Foo", "description": "There comes my hero"},
        {"name": "Red", "description": "It's my aeroplane"},
    ]


def test_omit(client):
    response = client.get("/omit")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Foo"},
        {"name": "Red"},
    ]


def test_pick(client):
    response = client.get("/pick")
    assert response.status_code == 200
    assert response.json() == [
        {"description": "There comes my hero"},
        {"description": "It's my aeroplane"},
    ]
