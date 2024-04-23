import pytest
import json
import logging


# Positive Tests
@pytest.mark.unit
def test_readings_views_get_all(api_client, create_test_readings, db):
    response = api_client.get("/products/1/devices/1/readings")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_readings_views_post(api_client, create_test_readings, db):
    file = {"readings": open(r"products\tests\readings.csv", "rb")}
    print(type(file["readings"]))
    response = api_client.post(
        "/products/1/devices/1/readings",
        file,
        format="multipart",
    )  # multipart/form-data
    assert response.status_code == 201


# Negative Tests
@pytest.mark.unit
def test_negative_readings_views_get_all_401(client):
    response = client.get("/products/1/devices/1/readings")
    data = json.loads(response.content)
    assert response.status_code == 401


@pytest.mark.unit
def test_negative_readings_views_post_401(client):
    file = {"readings": open(r"products\tests\readings.csv", "rb")}
    print(type(file["readings"]))
    response = client.post(
        "/products/1/devices/1/readings",
        file,
        format="multipart",
    )
    assert response.status_code == 401
