import pytest 
import json


@pytest.mark.unit
def test_readings_views_get_all(client, create_test_readings, db):
    response = client.get('/products/1/devices/1/readings')
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >=1


@pytest.mark.unit
def test_readings_views_post(client, create_test_readings, db):
    response = client.post('/products/1/devices/1/readings')
    assert response.status_code == 201
