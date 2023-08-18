from django.shortcuts import render

from .models import Survey
from .models import contactForm
from .forms import ContactFormForm
from django.http import HttpResponseRedirect

#Views Hompage
def home(request):
    return render(request, 'homepage.html')

def commons(request):
    return render(request, 'commons.html')

def about(request):
    return render(request, 'about.html')

def ratedfood(request):
    return render(request, 'ratedfood.html')