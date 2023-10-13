from django.shortcuts import render
from commons.views import parse_html as commons_parse_html, remove_items as commons_remove_items
from russellsage.views import parse_html as russellsage_parse_html, remove_items as russellsage_remove_items
from blitman.views import parse_html as blitman_parse_html, remove_items as blitman_remove_items


def home(request):
    return render(request, 'homepage.html')

def commons(request):
    commons_remove_items(request)
    return commons_parse_html(request)

def russellsage(request):
    russellsage_remove_items(request)
    return russellsage_parse_html(request)

def blitman(request):
    blitman_remove_items(request)
    return blitman_parse_html(request)