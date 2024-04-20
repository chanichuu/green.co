import pytest
import json


@pytest.mark.unit
def test_products_views_get_all(api_client, create_test_product, db):
    response = api_client.get("/products/")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_products_views_get_one(api_client, create_test_product, db):
    response = api_client.get("/products/1")
    data = json.loads(response.content)[0]
    assert response.status_code == 200
    assert data["pk"] == 1
    assert data["fields"]["name"] == "test-product"
    assert data["fields"]["image_link"] == "test-image-link"


@pytest.mark.unit
def test_product_views_post(api_client, create_test_product, db):
    data = {
        "name": "test-product",
        "image_link": "test-image-link",
    }
    response = api_client.post(
        "/products/",
        json.dumps(data),
        content_type="application/json",
    )
    print(response)
    assert response.status_code == 201


@pytest.mark.unit
def test_product_views_put(api_client, create_test_product, db):
    product = {
        "name": "test-product",
        "image_link": "test-image-link",
    }
    response = api_client.put(
        "/products/1",
        json.dumps(product),
        content_type="application/json",
    )
    data = response.content
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_product_views_delete(api_client, db):
    response = api_client.delete("/products/1")
    assert response.status_code == 204
