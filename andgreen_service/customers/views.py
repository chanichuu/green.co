from django.shortcuts import render
from django.http import HttpResponse
from customers.models import Customer
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def route_customer_requests_GET_POST(request):
    match request.method:
        case 'GET':
            return get_all_customers(request)
        case 'POST':
            return create_customer(request)


@api_view(['GET', 'PUT', 'DELETE'])
def route_customer_requests_GET_PUT_DELETE(request, id):
    match request.method:
        case 'GET':
            return get_customer(request, id)
        case 'PUT':
            return update_customer(request, id)
        case 'DELETE':
            return delete_customer(request, id)


def get_all_customers(request):
    # ----- YAML below for Swagger -----
    """
    Description: This API gets all customers.
    """
    customers = Customer.objects.all()
    return HttpResponse(
        serializers.serialize("json", customers),
        content_type="application/json"
    )


def get_customer(request, id):
    # ----- YAML below for Swagger -----
    """
    Description: This API gets a customer by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    try:
        customer = Customer.objects.get()
    except Customer.DoesNotExist:
        customer = None
        return HttpResponse('Customer not found.', status=404)
    
    return HttpResponse(
        serializers.serialize("json", customer),
        content_type="application/json"
    )


def create_customer(request, customer):
    # ----- YAML below for Swagger -----
    """
    Description: This API creates a new customer.
    """
    return HttpResponse("Created.", status=201)


def update_customer(request, id):
        # ----- YAML below for Swagger -----
    """
    Description: This API updates a customer.
    parameters:
    - name: id
        type: int
        required: true
    """
    return HttpResponse("Ok.", status=200)


def delete_customer(request, id):
    # ----- YAML below for Swagger -----
    """
    Description: This API deletes a customer by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    return HttpResponse("No content.", status=204)