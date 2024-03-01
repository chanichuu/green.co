import pytest
import json
import logging


@pytest.mark.unit
def test_readings_views_get_all(client, create_test_readings, db):
    response = client.get("/products/1/devices/1/readings")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_readings_views_post(client, create_test_readings, db):
    file = {"readings": open(r"products\tests\readings.csv", "rb")}
    print(type(file["readings"]))
    response = client.post(
        "/products/1/devices/1/readings",
        file,
        format="multipart/form-data",
    )  # multipart/form-data
    assert response.status_code == 201
