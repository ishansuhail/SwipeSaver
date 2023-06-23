from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to SwipeSaver!")

def commons(request):
    return HttpResponse("Welcome to Commons!")

def contact(request):
    return HttpResponse("Welcome to Contact!")

def about(request):
    return HttpResponse("Welcome to About!")