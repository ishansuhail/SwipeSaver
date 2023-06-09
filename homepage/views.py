from django.shortcuts import render

def home(request):
    return render(request, 'homepage.html')

def commons(request):
    return render(request, 'commons.html')
