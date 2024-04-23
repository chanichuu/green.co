from django.shortcuts import render
from django.http import HttpResponse
from customers.models import Customer
from django.core import serializers
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated
import json


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def route_customer_requests_GET_POST(request):
    match request.method:
        case "GET":
            return get_all_customers(request)
        case "POST":
            return create_customer(request)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def route_customer_requests_GET_PUT_DELETE(request, id):
    match request.method:
        case "GET":
            return get_customer(request, id)
        case "PUT":
            return update_customer(request, id)
        case "DELETE":
            return delete_customer(request, id)


def get_all_customers(request):
    # ----- YAML below for Swagger -----
    """
    Description: This API gets all customers.
    """
    customers = Customer.objects.all()
    return HttpResponse(
        serializers.serialize("json", customers), content_type="application/json"
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
        customer = Customer.objects.get(pk=id)
        return HttpResponse(
            serializers.serialize("json", [customer]), content_type="application/json"
        )
    except Customer.DoesNotExist:
        customer = None
        return HttpResponse("Customer not found.", status=404)


def create_customer(request):
    # ----- YAML below for Swagger -----
    """
    Description: This API creates a new customer.
    """
    try:
        data = request.body
        data = json.loads(data)
        print(data)
        customer = Customer.objects.create(
            username=data["username"],
            email=data["email"],
            pw=data["pw"],
            login_trials=data["login_trials"],
        )
        if data["products"]:
            customer.products.set(data["products"])

        return HttpResponse(
            serializers.serialize("json", [customer]),
            content_type="application/json",
            status=201,
        )
    except json.decoder.JSONDecodeError:
        return HttpResponse("Bad request.", status=400)


def update_customer(request, id):
    # ----- YAML below for Swagger -----
    """
    Description: This API updates a customer.
    parameters:
    - name: id
        type: int
        required: true
    """
    try:
        data = request.body
        data = json.loads(data)
        customer = Customer.objects.filter(pk=id).update(
            username=data["username"],
            email=data["email"],
            pw=data["pw"],
            login_trials=data["login_trials"],
        )
        if data["products"]:
            customer.products.set(data["products"])

        customer = Customer.objects.get(pk=id)

        return HttpResponse(
            serializers.serialize("json", [customer]),
            content_type="application/json",
            status=200,
        )
    except json.decoder.JSONDecodeError:
        return HttpResponse("Bad request.", status=400)


def delete_customer(request, id):
    # ----- YAML below for Swagger -----
    """
    Description: This API deletes a customer by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    Customer.objects.filter(pk=id).delete()
    return HttpResponse("No content.", status=204)
