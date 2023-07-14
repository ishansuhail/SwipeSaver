from django.shortcuts import render
from commons.views import parse_html

def home(request):
    return render(request, 'homepage.html')

def commons(request):
    return parse_html(request)
    #return render(request, 'commons.html')
