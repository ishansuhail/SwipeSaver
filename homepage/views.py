from django.shortcuts import render
from commons.views import parse_html as commons_parse_html, remove_items as commons_remove_items
from russellsage.views import parse_html as russellsage_parse_html, remove_items as russellsage_remove_items
<<<<<<< HEAD
from blitman.views import parse_html as blitman_parse_html, remove_items as blitman_remove_items
=======
>>>>>>> 382fd638787ec15e98cfcdd54181c22b7b7badf3


def home(request):
    return render(request, 'homepage.html')

def commons(request):
    commons_remove_items(request)
    return commons_parse_html(request)

def russellsage(request):
    russellsage_remove_items(request)
    return russellsage_parse_html(request)

<<<<<<< HEAD
def blitman(request):
    blitman_remove_items(request)
    return blitman_parse_html(request)
=======
>>>>>>> 382fd638787ec15e98cfcdd54181c22b7b7badf3
