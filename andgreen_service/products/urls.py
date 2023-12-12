from django.urls import path, re_path
from . import product_views, device_views, reading_views

urlpatterns = [
    path('', product_views.route_product_requests_GET_POST, name='GET_POST_ROUTER_PRODUCTS'),
    path('<int:pid>', product_views.route_product_requests_GET_PUT_DELETE, name='GET_PUT_DELETE_ROUTER_PRODUCTS'),
    path('<int:pid>/devices', device_views.route_device_requests_GET_POST, name='GET_POST_ROUTER_DEVICES'),
    path('<int:pid>/devices/<int:id>', device_views.route_device_requests_GET_PUT_DELETE, name='GET_PUT_DELETE_ROUTER_DEVICES'),
    path('<int:pid>/devices/<int:id>/readings', reading_views.route_readings_requests_GET_POST, name='GET_POST_ROUTER_READINGS'),
]