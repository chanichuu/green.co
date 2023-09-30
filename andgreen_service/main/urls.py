from django.urls import path
from . import views

urlpatterns = [
    path('main', views.get_homepage, name='getMain'),
    path('settings', views.get_settings, name='getSettings'),
]