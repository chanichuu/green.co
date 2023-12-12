import pytest 
from django.urls import reverse, resolve
from main.views import get_homepage, get_settings


@pytest.mark.unit
def test_getMain():
    path = reverse('home')
    assert resolve(path).view_name == 'home'


@pytest.mark.unit
def test_getSettings():
    path = reverse('settings')
    assert resolve(path).func == get_settings