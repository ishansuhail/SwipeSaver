from django.shortcuts import render
from commons.views import parse_html
from commons.views import remove_items
from russellsage.views import parse_html
from russellsage.views import remove_items

def home(request):
    return render(request, 'homepage.html')

def commons(request):
    remove_items(request)
    return parse_html(request)
    #return render(request, 'commons.html')

def russellsage(request):
    remove_items(request)
    return parse_html(request)
    #return render(request, 'russellsage.html')
