from django.urls import path, re_path
from . import product_views, device_views, reading_views

urlpatterns = [
    path('', product_views.route_product_requests_GET_POST, name='GET_POST_ROUTER_PRODUCTS'),
    path('<int:id>', product_views.route_product_requests_GET_PUT_DELETE, name='GET_PUT_DELETE_ROUTER_PRODUCTS'),
    path('devices/', device_views.route_device_requests_GET_POST, name='GET_POST_ROUTER_DEVICES'),
    path('devices/<int:id>', device_views.route_device_requests_GET_PUT_DELETE, name='GET_PUT_DELETE_ROUTER_DEVICES'),
    path('devices/<int:id>/readings', reading_views.create_readings, name='CREATE_READINGS'),
    re_path(r'^devices/<int:id>/readings/$', reading_views.get_readings, name='GET_READINGS'),
]