import pytest
import json
from customers.models import Customer


# Positive Tests
@pytest.mark.unit
def test_customer_views_get_all(api_client, create_test_customer, db):
    response = api_client.get("/customers/")
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_customer_views_get(api_client, create_test_customer, db):
    response = api_client.get("/customers/1")
    data = json.loads(response.content)[0]
    print(data)
    assert response.status_code == 200
    assert data["pk"] == 1
    assert data["fields"]["username"] == "Test User"
    assert data["fields"]["email"] == "test-user@gmail.com"


@pytest.mark.unit
def test_customer_views_post(api_client, create_test_customer, db):
    data = {
        "username": "Test User",
        "email": "testUser@gmail.com",
        "pw": "testpassword",
        "login_trials": 5,
        "products": [],
    }
    response = api_client.post(
        "/customers/",
        json.dumps(data),
        content_type="application/json",
    )

    assert response.status_code == 201


@pytest.mark.unit
def test_customer_views_put(api_client, create_test_customer, db):
    customer = {
        "username": "Test User Updated",
        "email": "testUserUpdated@gmail.com",
        "pw": "testpasswordUpdated",
        "login_trials": 5,
        "products": [],
    }
    response = api_client.put(
        "/customers/1",
        json.dumps(customer),
        content_type="application/json",
    )
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(data) >= 1


@pytest.mark.unit
def test_customer_views_delete(api_client, db):
    response = api_client.delete("/customers/1")
    assert response.status_code == 204


# Negative Tests
@pytest.mark.unit
def test_negative_customer_views_get_all_401(client):
    response = client.get("/customers/")
    data = json.loads(response.content)
    assert response.status_code == 401


@pytest.mark.unit
def test_negative_customer_views_get_401(client):
    response = client.get("/customers/1")
    data = json.loads(response.content)
    assert response.status_code == 401


@pytest.mark.unit
def test_negative_customer_views_post_401(client):
    data = {
        "username": "Test User",
        "email": "testUser@gmail.com",
        "pw": "testpassword",
        "login_trials": 5,
        "products": [],
    }
    response = client.post(
        "/customers/",
        json.dumps(data),
        content_type="application/json",
    )

    assert response.status_code == 401


@pytest.mark.unit
def test_negative_customer_views_put_401(client):
    customer = {
        "username": "Test User Updated",
        "email": "testUserUpdated@gmail.com",
        "pw": "testpasswordUpdated",
        "login_trials": 5,
        "products": [],
    }
    response = client.put(
        "/customers/1",
        json.dumps(customer),
        content_type="application/json",
    )
    data = json.loads(response.content)
    assert response.status_code == 401


@pytest.mark.unit
def test_negative_customer_views_delete_401(client):
    response = client.delete("/customers/1")
    assert response.status_code == 401
