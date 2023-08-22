from django.urls import path
from . import views

urlpatterns = [
    path('health', views.health, name='health'),
    path('version', views.version, name='version'),
    path('restversion', views.rest_version, name='rest_version')
]