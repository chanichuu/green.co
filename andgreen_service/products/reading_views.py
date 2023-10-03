from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.core import serializers
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_readings(request, startTime, endTime):
    """
    Description: This API gets all readings within a start and end time range in milliseconds.
    parameters:
    - name: start
        type: int
        required: true
    - name: end
        type: int
        required: true
    """
    products = Product.objects.all()

    return HttpResponse(
        serializers.serialize("json", products),
        content_type="application/json"
    )


@api_view(['POST'])
def create_readings(request):
    """
    Description: This API imports readings.
    """
    return HttpResponse("Created.", status=201)