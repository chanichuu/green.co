from django.shortcuts import render
from django.http import HttpResponse
from products.models import Device, Product
from django.core import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def route_device_requests_GET_POST(request, pid):
    match request.method:
        case "GET":
            return get_all_devices(request, pid)
        case "POST":
            return create_device(request, pid)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def route_device_requests_GET_PUT_DELETE(request, pid, id):
    match request.method:
        case "GET":
            return get_device(request, pid, id)
        case "PUT":
            return update_device(request, pid, id)
        case "DELETE":
            return delete_device(request, pid, id)


def get_all_devices(request, pid):
    """
    Description: This API gets all devices.
    """
    devices = Device.objects.all()

    return HttpResponse(
        serializers.serialize("json", devices), content_type="application/json"
    )


def get_device(request, pid, id):
    """
    Description: This API gets a device by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    try:
        device = Device.objects.get(id=id)
        print(f"device: {device}")

        return HttpResponse(
            serializers.serialize("json", [device]), content_type="application/json"
        )
    except Device.DoesNotExist:
        device = None
        return HttpResponse("Device not found.", status=404)


def create_device(request, pid):
    """
    Description: This API creates a new device.
    """
    try:
        product = _get_product(pid)
        data = json.loads(request.body)
        device = Device.objects.create(description=data["description"], product=product)

        return HttpResponse(
            serializers.serialize("json", [device]),
            content_type="application/json",
            status=201,
        )
    except json.decoder.JSONDecodeError:
        return HttpResponse("Bad request.", status=400)


def update_device(request, pid, id):
    """
    Description: This API updates a device.
    parameters:
    - name: id
        type: int
        required: true
    """
    try:
        product = _get_product(pid)
        data = json.loads(request.body)
        device = Device.objects.filter(pk=id).update(
            description=data["description"], product=product
        )

        device = Device.objects.get(pk=id)
        return HttpResponse(
            serializers.serialize("json", [device]),
            content_type="application/json",
            status=200,
        )
    except json.decoder.JSONDecodeError:
        return HttpResponse("Bad request.", status=400)


def delete_device(request, pid, id):
    """
    Description: This API deletes a device by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    Device.objects.filter(pk=id).delete()
    return HttpResponse("No content.", status=204)


def _get_product(pid):
    try:
        product = Product.objects.get(pk=pid)
        return product
    except Product.DoesNotExist:
        device = None
        return HttpResponse("Bad request: Device not found.", status=400)
