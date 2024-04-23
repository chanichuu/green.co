from django.urls import path
from . import views

urlpatterns = [
    path('', views.route_customer_requests_GET_POST, name='GET_POST_ROUTER'),
    path('<int:id>', views.route_customer_requests_GET_PUT_DELETE, name='GET_PUT_DELETE_ROUTER'),
]