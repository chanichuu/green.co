import pytest 
import json


@pytest.mark.unit
def test_products_views_get_all(client, create_test_product, db):
    response = client.get('/products/')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_products_views_get_one(client, create_test_product, db):
    response = client.get('/products/1')
    data = json.loads(response.content)[0]
    print(data)
    assert response.status_code == 200
    assert data['pk'] == 1
    assert data['fields']['name'] == 'test-product'
    assert data['fields']['image_link'] == 'test-image-link'


