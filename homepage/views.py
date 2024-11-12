from django.shortcuts import render
from commons.views import commons as commons_view
from barh.views import barh as barh_view
from russellsage.views import russellsage as russellsage_view
from blitman.views import blitman as blitman_view

def home(request):
    return render(request, 'homepage.html')

def commons(request):
     return commons_view(request)

def barh(request):
    return barh_view(request)

def russellsage(request):
    return russellsage_view(request)

def blitman(request):
    return blitman_view(request)
