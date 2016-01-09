from django.shortcuts import render
from django.http import HttpResponse, Http404

def home(request):
    output = "Welcome to the homepage!"
    return HttpResponse(output)
