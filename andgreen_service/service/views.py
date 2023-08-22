from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def health(request):
    return HttpResponse('Service is healthy.')

def version(request):
    return HttpResponse('0.0.1')

def rest_version(request):
    return HttpResponse('v0')