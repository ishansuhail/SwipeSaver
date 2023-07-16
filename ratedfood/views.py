from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def commons(request):
    return render(request, 'commons.html')

def contact(request):
	
	form = ContactFormForm
	return render(request, 'contact.html', {'form':form})

def about(request):
	return render(request, 'contact.html')

def ratedfood(request):
	return render(request, 'ratedfood.html')
