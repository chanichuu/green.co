import pytest
import json


@pytest.mark.unit
def test_device_views_get_all(api_client, create_test_device, db):
    response = api_client.get("/products/1/devices")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_device_views_get_one(api_client, create_test_device, db):
    response = api_client.get("/products/1/devices/1")
    data = json.loads(response.content)[0]
    print(data)
    assert response.status_code == 200
    assert data["pk"] == 1
    assert data["fields"]["description"] == "test-device"


@pytest.mark.unit
def test_device_views_post(api_client, create_test_device, db):
    product = {
        "name": "test-product",
        "image_link": "test-image-link",
    }
    data = {
        "description": "test-device",
        "product": product,
    }
    response = api_client.post(
        "/products/1/devices",
        json.dumps(data),
        content_type="application/json",
    )
    print(response)
    assert response.status_code == 201


@pytest.mark.unit
def test_device_views_put(api_client, create_test_device, db):
    product = {
        "name": "test-product",
        "image_link": "test-image-link",
    }
    data = {
        "description": "test-device updated",
        "product": product,
    }
    response = api_client.put(
        "/products/1/devices/1",
        json.dumps(data),
        content_type="application/json",
    )
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_device_views_delete(api_client, db):
    response = api_client.delete("/products/1/devices/1")
    assert response.status_code == 204
