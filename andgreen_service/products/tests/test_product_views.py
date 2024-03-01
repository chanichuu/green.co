import pytest
import json


@pytest.mark.unit
def test_products_views_get_all(client, create_test_product, db):
    response = client.get("/products/")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_products_views_get_one(client, create_test_product, db):
    response = client.get("/products/1")
    data = json.loads(response.content)[0]
    assert response.status_code == 200
    assert data["pk"] == 1
    assert data["fields"]["name"] == "test-product"
    assert data["fields"]["image_link"] == "test-image-link"


@pytest.mark.unit
def test_product_views_post(client, create_test_product, db):
    data = {
        "name": "test-product",
        "image_link": "test-image-link",
    }
    response = client.post(
        "/products/",
        data,
        content_type="application/json",
    )
    print(response)
    assert response.status_code == 201


@pytest.mark.unit
def test_product_views_put(client, create_test_product, db):
    product = {
        "name": "test-product",
        "image_link": "test-image-link",
    }
    response = client.put(
        "/products/1",
        product,
        content_type="application/json",
    )
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_product_views_delete(client, db):
    response = client.delete("/products/1")
    assert response.status_code == 204
