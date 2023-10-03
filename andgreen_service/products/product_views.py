from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.core import serializers
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def route_product_requests_GET_POST(request):
    match request.method:
        case 'GET':
            return get_all_products(request)
        case 'POST':
            return create_product(request)


@api_view(['GET', 'PUT', 'DELETE'])
def route_product_requests_GET_PUT_DELETE(request, id):
    match request.method:
        case 'GET':
            return get_product(request, id)
        case 'PUT':
            return update_product(request, id)
        case 'DELETE':
            return delete_product(request, id)


def get_all_products(request):
    """
    Description: This API gets all products.
    """
    products = Product.objects.all()

    return HttpResponse(
        serializers.serialize("json", products),
        content_type="application/json"
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
    except Product.DoesNotExist:
        product = None
        return HttpResponse('Product not found.', status=404)
    
    return HttpResponse(
        serializers.serialize("json", product),
        content_type="application/json"
    )


def create_product(request):
    """
    Description: This API creates a new product.
    """
    return HttpResponse("Created.", status=201)
    

def update_product(request, id):
    """
    Description: This API updates a product.
    parameters:
    - name: id
        type: int
        required: true
    """
    return HttpResponse("Ok.", status=200)


def delete_product(request, id):
    """
    Description: This API deletes a product by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    return HttpResponse("No content.", status=204)