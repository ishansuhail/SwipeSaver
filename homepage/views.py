from django.shortcuts import render

def home(request):
    return render(request, 'homepage/homepage.html')

def commons(request):
    return render(request, 'homepage/commons.html')
