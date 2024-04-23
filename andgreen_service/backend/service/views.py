from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def health(request):
    """
    Description: This API gets health state of the service.
    """
    return HttpResponse("Service is healthy.")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def version(request):
    """
    Description: This API gets current service version.
    """
    return HttpResponse("0.0.1")


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def rest_version(request):
    """
    Description: This API gets current REST API service version.
    """
    return HttpResponse("v0")
