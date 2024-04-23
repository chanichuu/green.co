import pytest
import json
import os


# Positive Tests
@pytest.mark.unit
def test_CreateUserView(client, db):
    test_name = "marie"
    data = {
        "username": test_name,
        "password": os.getenv("TEST_PASSWORD"),
    }
    response = client.post("/users/register/", data)
    data = json.loads(response.content)
    print(f"User create response: {data}")
    assert response.status_code == 201
    assert len(data) >= 1
    assert data["username"] == test_name


@pytest.mark.unit
def test_UserListCreate(api_client, db):
    response = api_client.get("/users/current/")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1
    assert data[0]["username"] == os.getenv("TEST_USERNAME")


# Negative Tests
@pytest.mark.unit
def test_Negative_CreateUserView_400(client, db):
    data = {
        "username": os.getenv("TEST_USERNAME"),
        "password": os.getenv("TEST_PASSWORD"),
    }
    response = client.post("/users/register/", data)
    data = json.loads(response.content)
    assert response.status_code == 400


@pytest.mark.unit
def test_Negative_UserListCreate_401(client, db):
    response = client.get("/users/current/")
    data = json.loads(response.content)
    assert response.status_code == 401
