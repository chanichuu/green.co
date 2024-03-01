import pytest
import json
from customers.models import Customer


@pytest.mark.unit
def test_customer_views_get_all(client, create_test_customer, db):
    response = client.get("/customers/")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_customer_views_get(client, create_test_customer, db):
    response = client.get("/customers/1")
    data = json.loads(response.content)[0]
    print(data)
    assert response.status_code == 200
    assert data["pk"] == 1
    assert data["fields"]["username"] == "Test User"
    assert data["fields"]["email"] == "test-user@gmail.com"


@pytest.mark.unit
def test_customer_views_post(client, create_test_customer, db):
    data = {
        "username": "Test User",
        "email": "testUser@gmail.com",
        "pw": "testpassword",
        "login_trials": 5,
        "products": [],
    }
    response = client.post(
        "/customers/",
        data,
        content_type="application/json",
    )

    assert response.status_code == 201


@pytest.mark.unit
def test_customer_views_put(client, create_test_customer, db):
    customer = {
        "username": "Test User Updated",
        "email": "testUserUpdated@gmail.com",
        "pw": "testpasswordUpdated",
        "login_trials": 5,
        "products": [],
    }
    response = client.put(
        "/customers/1",
        customer,
        content_type="application/json",
    )
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_customer_views_delete(client, db):
    response = client.delete("/customers/1")
    assert response.status_code == 204
