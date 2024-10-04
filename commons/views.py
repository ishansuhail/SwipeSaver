# Standard Library Imports
import datetime
import re
import json

# Third-Party Library Imports
from bs4 import BeautifulSoup
import requests
from unidecode import unidecode

# Django Imports
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Avg

# Local Application Imports
from populate_db.views import populate
from populate_db.models import FoodItem
from .models import Rating, Station




def commons(request):
    #populate(url = "https://rpi.sodexomyway.com/en-us/locations/the-commons-dining-hall")

    food_items = FoodItem.objects.using('PostgresDB').filter(dining_hall="commons")

    for item in food_items:
        print(f"Name: {item.name}")
        print(f"Description: {item.description}")
        print(f"Meal: {item.meal}")
        print(f"Station: {item.station}")
        print(f"Dining Hall: {item.dining_hall}")
        print("---")  # Separator for readability
    
    # Pass the result to the template
    return render(request, 'commons.html', {'food_items': food_items})
    
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def rate(request):
    if is_ajax(request):
        rating_val = None
        station_name = None
        meal_time = None
        for key, value in request.GET.items():  # loop through all GET parameters
            if 'rating' in key:
                parts = key.split('-')
                rating_val = value
                meal_time = parts[1]  # get the meal time from the parameter key
                station_name = parts[2]  # get the station name from the parameter key

        if rating_val is not None:
            rating_val = int(rating_val)
            station, _ = Station.objects.get_or_create(name=station_name.capitalize())
            rating = Rating(station=station, rating=rating_val, meal_time=meal_time)
            rating.save()

            # Calculate the average rating
            today = datetime.date.today()
            average_rating = Rating.objects.filter(station=station, meal_time=meal_time, date=today).aggregate(Avg('rating'))['rating__avg']
            if average_rating is not None:
                average_rating = round(average_rating, 2)  # round to 2 decimal places

            return JsonResponse({'success': True, 'average_rating': average_rating})
    return JsonResponse({'success': False})


