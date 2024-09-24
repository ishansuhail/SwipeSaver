from django.shortcuts import render

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
    populate()
    return render(request, 'commons.html')


def populate(url = "https://rpi.sodexomyway.com/en-us/locations/the-commons-dining-hall"):
    response = requests.get(url)
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tag = soup.find('script', text=re.compile(r'window\.__PRELOADED_STATE__'))
    if script_tag:
        script_content = script_tag.string

        # print(script_content)
        split_content = script_content.split('window.__PRELOADED_STATE__ = ')
        
        if split_content:
        # Print the parts before and after the split
        # print("Part before 'window.__PRELOADED_STATE__':")
        # print(split_content[0].strip())  # Part before the delimiter
        # print("\nPart after 'window.__PRELOADED_STATE__':")
            try: 
                json_data = json.loads(split_content[1].strip())  # Parse the JSON string into a Python dictionary
                file_name = 'output.txt'  # You can change this to any file name or path

# Open the file in write mode and save the content
                with open(file_name, 'w', encoding='utf-8') as file:
                    data = json_data.get('composition').get('subject').get('regions')[1].get('fragments')[0].get('content').get('main').get('sections')
                    print(data[0].get('name'))
                    print(data[1].get('name'))
                    print(data[2].get('name'))
                    file.write(json.dumps(data, indent= 2))
                # Get the ratings data
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)  # Part after the delimiter
        
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


