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


def br_lunch_day():
    current_date = datetime.date.today()
    day = current_date.weekday()
    
    return day
    

def dinner_day():
    current_date = datetime.date.today()
    day = current_date.weekday()
    if(day == 6):
        return 0
    day += 1
    
    return day

def parse_html(request):
    
    
    with open('commons/templates/commons.html', 'r') as file:
        existing_html = file.read()
    if '<hr class="dashed-line">' in existing_html:
        return render(request, 'commons.html')
    
    # Perform the parsing and modification logic
    r = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall")
    html_content = r.content

    soup = BeautifulSoup(html_content, 'html.parser')
    br_lunch = br_lunch_day()
    dinner = dinner_day()
    
    parse_meal(soup, 'accordion-block breakfast', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 10px; margin-left: 68px; margin-bottom: 5px">BREAKFAST (7:00 - 9:30)</p>', br_lunch)
    parse_meal(soup, 'accordion-block lunch', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px;margin-bottom: 5px">LUNCH (11:00 - 3:00)</p>', br_lunch)
    parse_meal(soup, 'accordion-block dinner', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">DINNER (4:30 - 8:00)</p>', dinner)

    # parse_meal(soup, 'accordion-block breakfast', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 10px; margin-left: 68px; margin-bottom: 5px">BREAKFAST (7:00 - 9:30)</p>')
    # parse_meal(soup, 'accordion-block lunch', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px;margin-bottom: 5px">LUNCH (11:00 - 3:00)</p>')
    # parse_meal(soup, 'accordion-block dinner', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">DINNER (4:30 - 8:00)</p>')

    return render(request, 'commons.html')  # Render the modified template


def parse_meal(soup, meal, html_pattern, day):
    meal_type = soup.find_all('div', class_= meal)

    with open('commons/templates/commons.html', "r") as file:
        existing_html = file.read()
        
    meal_string = str(meal_type[day])
    pattern = r'data-fooditemname="([^"]+)"'
    result = re.findall(pattern, meal_string)

    if result:
            
        search_pattern = html_pattern + '\n<button class="accordion">Grill</button>\n<div class="panel">\n'
        index = existing_html.find(search_pattern)

        if index != -1:
            # Calculate the insertion index
            insertion_index = index + len(search_pattern)
            modified_html = existing_html[:insertion_index]

            for item in result:
                if item != result[-1]:
                    modified_html += f'\t\t<p style="font-size: 24px; margin-top: 25px; margin-left: 30px">{item}</p>\n\t\t<hr class="dashed-line">\n'
                else:
                    modified_html += f'\t\t<p style="font-size: 24px; margin-top: 25px; margin-left: 30px">{item}</p>\n\t\t<hr class="dashed-line">'
                    
            modified_html += existing_html[insertion_index:]

            with open("commons/templates/commons.html", "w") as file:
                file.write(modified_html)

# def parse_meal(soup, meal, html_pattern):
#     meal_type = soup.find_all('div', class_= meal)

#     with open('commons/templates/commons.html', "r") as file:
#         existing_html = file.read()

#     current_date = datetime.date.today()
#     day = current_date.weekday()
    
#     count = 0
#     for i in meal_type:
        
#         meal_string = str(i)
#         pattern = r'data-fooditemname="([^"]+)"'
#         result = re.findall(pattern, meal_string)

#         if result:
            
#             search_pattern = html_pattern + '\n<button class="accordion">Grill</button>\n<div class="panel">\n'
#             index = existing_html.find(search_pattern)

#             if index != -1:
#                 # Calculate the insertion index
#                 insertion_index = index + len(search_pattern)
#                 modified_html = existing_html[:insertion_index]

#                 for item in result:
#                     modified_html += f'\t\t<p style="font-size: 24px; margin-top: 25px; margin-left: 30px">{item} {day_} {current_date} {len(meal_type)} </p>\n\t\t<hr class="dashed-line">\n'
                    
#                 modified_html += existing_html[insertion_index:]

#                 with open("commons/templates/commons.html", "w") as file:
#                     file.write(modified_html)
#         count += 1

 #remove the food items
def remove_items(request):
    with open('commons/templates/commons.html', 'r') as file:
        file_change = file.read()
    
    soup = BeautifulSoup(file_change, 'html.parser')
    
    elements = soup.find_all('p', style = 'font-size: 24px; margin-top: 25px; margin-left: 30px')
    
    for element in elements:
        element.extract()
    
    second_elements = soup.find_all('hr', class_ = 'dashed-line')
    
    for element in second_elements:
        element.extract()
    
    
    with open('commons/templates/commons.html', 'w') as file:
        file.write(str(soup))
    
    return render(request, 'commons.html')



    
def home(request):
    return HttpResponse("Welcome to SwipeSaver!")

def commons(request):
    return HttpResponse("Welcome to Commons!")

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def rate(request):
    print("Made it here")
    if is_ajax(request):
        print("inside is_ajax")
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
            average_rating = Rating.objects.filter(station=station, meal_time=meal_time).aggregate(Avg('rating'))['rating__avg']
            if average_rating is not None:
                average_rating = round(average_rating, 2)  # round to 2 decimal places

            return JsonResponse({'success': True, 'average_rating': average_rating})
    return JsonResponse({'success': False})

