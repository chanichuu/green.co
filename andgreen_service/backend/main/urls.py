from django.urls import path
from . import views
from django.views.generic.base import TemplateView 


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('settings', views.get_settings, name='settings'),
]