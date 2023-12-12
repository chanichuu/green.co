import pytest 
import json


@pytest.mark.unit
def test_devices_views_get_all(client, create_test_device, db):
    response = client.get('/products/1/devices')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_devices_views_get_one(client, create_test_device, db):
    response = client.get('/products/1/devices/1')
    data = json.loads(response.content)[0]
    print(data)
    assert response.status_code == 200
    assert data['pk'] == 1
    assert data['fields']['description'] == 'test-device'
