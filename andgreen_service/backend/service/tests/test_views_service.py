import pytest
import json


# Positive Tests
@pytest.mark.unit
def test_health(api_client, db):
    response = api_client.get("/service/health")
    data = response.content.decode("UTF-8")
    assert response.status_code == 200
    assert data == "Service is healthy."


@pytest.mark.unit
def test_version(api_client, db):
    response = api_client.get("/service/version")
    data = response.content.decode("UTF-8")
    assert response.status_code == 200
    assert data == "0.0.1"


@pytest.mark.unit
def test_rest_version(api_client, db):
    response = api_client.get("/service/restversion")
    data = response.content.decode("UTF-8")
    assert response.status_code == 200
    assert data == "v0"


# Negative Tests
@pytest.mark.unit
def test_negative_health_401(client):
    response = client.get("/service/health")
    assert response.status_code == 401


@pytest.mark.unit
def test_negative_version_401(client):
    response = client.get("/service/version")
    assert response.status_code == 401


@pytest.mark.unit
def test_negative_rest_version_401(client):
    response = client.get("/service/restversion")
    assert response.status_code == 401
