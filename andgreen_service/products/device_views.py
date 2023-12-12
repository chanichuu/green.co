from django.shortcuts import render
from django.http import HttpResponse
from products.models import Device
from django.core import serializers
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def route_device_requests_GET_POST(request, pid):
    match request.method:
        case 'GET':
            return get_all_devices(request, pid)
        case 'POST':
            return create_device(request, pid)


@api_view(['GET', 'PUT', 'DELETE'])
def route_device_requests_GET_PUT_DELETE(request, pid, id):
    match request.method:
        case 'GET':
            return get_device(request, pid, id)
        case 'PUT':
            return update_device(request, pid, id)
        case 'DELETE':
            return delete_device(request, pid, id)


def get_all_devices(request, pid):
    """
    Description: This API gets all devices.
    """
    devices = Device.objects.all()

    return HttpResponse(
        serializers.serialize("json", devices),
        content_type="application/json"
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
        print(f'device: {device}')
              
        return HttpResponse(
            serializers.serialize("json", [device]),
            content_type="application/json"
        )
    except Device.DoesNotExist:
        device = None
        return HttpResponse('Device not found.', status=404)


def create_device(request, pid):
    """
    Description: This API creates a new device.
    """
    return HttpResponse("Created.", status=201)
    

def update_device(request, pid, id):
    """
    Description: This API updates a device.
    parameters:
    - name: id
        type: int
        required: true
    """
    return HttpResponse("Ok.", status=200)


def delete_device(request, pid, id):
    """
    Description: This API deletes a device by id.
    parameters:
    - name: id
        type: int
        required: true
    """
    return HttpResponse("No content.", status=204)