from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.core import serializers
from rest_framework.decorators import api_view
import json


@api_view(["GET", "POST"])
def route_product_requests_GET_POST(request):
    match request.method:
        case "GET":
            return get_all_products(request)
        case "POST":
            return create_product(request)


@api_view(["GET", "PUT", "DELETE"])
def route_product_requests_GET_PUT_DELETE(request, pid):
    match request.method:
        case "GET":
            return get_product(request, pid)
        case "PUT":
            return update_product(request, pid)
        case "DELETE":
            return delete_product(request, pid)


def get_all_products(request):
    """
    Description: This API gets all products.
    """
    products = Product.objects.all()

    return HttpResponse(
        serializers.serialize("json", products), content_type="application/json"
    )


def get_product(request, id):
    """
    Description: This API gets a product by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    try:
        product = Product.objects.get(id=id)
        print(product.name)
        return HttpResponse(
            serializers.serialize("json", [product]), content_type="application/json"
        )
    except Product.DoesNotExist:
        product = None
        return HttpResponse("Product not found.", status=404)


def create_product(request):
    """
    Description: This API creates a new product.
    """
    try:
        data = json.loads(request.body)
        product = Product.objects.create(
            name=data["name"],
            image_link=data["image_link"],
        )
        return HttpResponse(
            serializers.serialize("json", [product]),
            content_type="application/json",
            status=201,
        )
    except json.decoder.JSONDecodeError:
        return HttpResponse("Bad request.", status=400)


def update_product(request, id):
    """
    Description: This API updates a product.
    parameters:
    - name: id
        type: int
        required: true
    """
    try:
        data = json.loads(request.body)
        Product.objects.filter(pk=id).update(
            name=data["name"],
            image_link=data["image_link"],
        )
        product = Product.objects.get(pk=id)
        return HttpResponse(
            serializers.serialize("json", [product]),
            content_type="application/json",
            status=200,
        )
    except json.decoder.JSONDecodeError:
        return HttpResponse("Bad request.", status=400)


def delete_product(request, id):
    """
    Description: This API deletes a product by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    Product.objects.filter(pk=id).delete()
    return HttpResponse("No content.", status=204)
