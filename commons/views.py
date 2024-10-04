from django.shortcuts import render
from populate_db.views import populate

import datetime

from django.http import JsonResponse
from django.db.models import Avg
from .models import Rating, Station
# Create your views here.
from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests
import re
import json
from unidecode import unidecode



def commons(request):
    populate(url = "https://rpi.sodexomyway.com/en-us/locations/the-commons-dining-hall")
    return render(request, 'commons.html')



        
        # if s:
        #     json_data_str = json_data_match.group(1)  # Extract the matched JSON string
            
        #     try:
        #         # Step 3: Parse the JSON string into a Python dictionary
        #         json_data = json.loads(json_data_str)
                
        #         # Print the extracted JSON data
        #         print(json.dumps(json_data, indent=4))  # Pretty print the JSON data
        #     except json.JSONDecodeError as e:
        #         print("Error decoding JSON:", e)
        # else:
        #     print("No JSON data found.")
    


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


