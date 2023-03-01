from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def owner(request):
    return HttpResponse("Hello world!")

def home(request):
    return HttpResponse('homepage')