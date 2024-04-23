# Define fixtures here
import pytest
from products.models import Product, Reading, Device
from customers.models import Customer
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
import os


# Customers
@pytest.fixture(scope="module")
def create_test_customer(django_db_blocker):
    with django_db_blocker.unblock():
        test_product = Product.objects.create(
            name="test-product", image_link="test-image-link"
        )
        customer = Customer.objects.create(
            username="Test User",
            email="test-user@gmail.com",
            pw="testpw",
            login_trials=5,
        )
        customer.products.set([test_product])
        return customer


# Products
@pytest.fixture(scope="module")
def create_test_product(django_db_blocker):
    with django_db_blocker.unblock():
        return Product.objects.create(name="test-product", image_link="test-image-link")


# Devices
@pytest.fixture(scope="module")
def create_test_device(django_db_blocker):
    with django_db_blocker.unblock():
        product = Product.objects.create(
            name="test-product", image_link="test-image-link"
        )
        return Device.objects.create(product=product, description="test-device")


# Readings
@pytest.fixture(scope="module")
def create_test_readings(django_db_blocker):
    with django_db_blocker.unblock():
        product = Product.objects.create(
            name="test-product", image_link="test-image-link"
        )
        device = Device.objects.create(product=product, description="test-device")
        return Reading.objects.create(
            timestamp="2016-05-18T15:37:36.993048Z",
            device=device,
            ppm_co2_water=2.5,
            ppm_co2_air=1.5,
            water_temp=15,
        )


# Users - Auth
@pytest.fixture(scope="package")
def api_client(django_db_blocker):
    with django_db_blocker.unblock():
        user = User.objects.create_user(
            username=os.getenv("TEST_USERNAME"),
            email=os.getenv("TEST_EMAIL"),
            password=os.getenv("TEST_PASSW"),
        )
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

        return client
