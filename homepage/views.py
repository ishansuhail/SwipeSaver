from django.shortcuts import render
from commons.views import commons as commons_view
from barh.views import parse_html as barh_parse_html, remove_items as barh_remove_items
from russellsage.views import russellsage as russellsage_view
from blitman.views import parse_html as blitman_parse_html, remove_items as blitman_remove_items


def home(request):
    return render(request, 'homepage.html')

def commons(request):
     return commons_view(request)

def barh(request):
    barh_remove_items(request)
    return barh_parse_html(request)

def russellsage(request):
    return russellsage_view(request)

def blitman(request):
    blitman_remove_items(request)
    return blitman_parse_html(request)
