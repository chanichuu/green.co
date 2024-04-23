from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_homepage(request):
    return HttpResponse("Homepage")


def get_settings(request):
    return HttpResponse("Settings")