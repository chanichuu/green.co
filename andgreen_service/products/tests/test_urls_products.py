import pytest 
from django.urls import reverse, resolve
from products.product_views import route_product_requests_GET_POST, route_product_requests_GET_PUT_DELETE
from products.device_views import route_device_requests_GET_POST, route_device_requests_GET_PUT_DELETE
from products.reading_views import route_readings_requests_GET_POST


@pytest.mark.unit
def test_products_urls_get_all():
    path = reverse('GET_POST_ROUTER_PRODUCTS')
    assert resolve(path).func == route_product_requests_GET_POST


@pytest.mark.unit
def test_products_urls_get_one():
    path = reverse('GET_PUT_DELETE_ROUTER_PRODUCTS', args=[1])
    assert resolve(path).func == route_product_requests_GET_PUT_DELETE


@pytest.mark.unit
def test_devices_urls_get_all():
    path = reverse('GET_POST_ROUTER_DEVICES', args=[1])
    assert resolve(path).func == route_device_requests_GET_POST


@pytest.mark.unit
def test_devices_urls_get_one():
    path = reverse('GET_PUT_DELETE_ROUTER_DEVICES', args=[1, 1])
    assert resolve(path).func == route_device_requests_GET_PUT_DELETE


@pytest.mark.unit
def test_readings_urls_get_all():
    path = reverse('GET_POST_ROUTER_READINGS', args=[1, 1])
    assert resolve(path).func == route_readings_requests_GET_POST