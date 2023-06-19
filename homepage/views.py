from django.shortcuts import render

from .models import Survey
from .models import contactForm
from .forms import ContactFormForm

def home(request):
    return render(request, 'homepage.html')

def commons(request):
    return render(request, 'commons.html')

def contact(request):
    form = ContactFormForm
    return render(request, 'contact.html', {'form':form})

def about(request):
    return render(request, 'about.html')