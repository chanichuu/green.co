import pytest
from django.urls import reverse, resolve
from service.views import health, version, rest_version

@pytest.mark.unit
def test_url_health():
    path = reverse('health')
    assert resolve(path).func == health

@pytest.mark.unit
def test_url_version():
    path = reverse('version')
    assert resolve(path).func == version

@pytest.mark.unit
def test_url_rest_version():
    path = reverse('rest_version')
    assert resolve(path).func == rest_version