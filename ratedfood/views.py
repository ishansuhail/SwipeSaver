from django.shortcuts import render
from .models import ratedFoodItem


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
    temp_food = ratedFoodItem(food_name="temp", image="temp.jpg", rating=4.5, vegan=False)
    temp_food.save()

   
    display_FOOD = ratedFoodItem.objects.all()
    return render(request, 'ratedfood.html', {'display_FOOD': display_FOOD})

def display_FOOD(request):
	display_FOOD = ratedFoodItem.objects.all()
	return render(request, 'display_FOOD.html', {'display_FOOD': display_FOOD})
