from django.shortcuts import render

from .models import Survey
from .models import contactForm
from .forms import ContactFormForm

from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'homepage.html')

def commons(request):
    return render(request, 'commons.html')

def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            #form.save() error?
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactFormForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'contact.html', {'form':form, 'submitted':submitted})

def about(request):
    return render(request, 'about.html')

def ratedfood(request):
    return render(request, 'ratedfood.html')