from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getAllProducts(request):
    return HttpResponse('No products yet.')