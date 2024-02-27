from django.shortcuts import render

import datetime
import sqlite3

from django.http import JsonResponse
from django.db.models import Avg
from .models import Rating, Station
# Create your views here.
from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests
import re
from unidecode import unidecode




def br_lunch_day():
    current_date = datetime.date.today()
    day = current_date.weekday()
    #day = 5
    return day
    

def dinner_day():
    current_date = datetime.date.today()
    day = current_date.weekday()
    #day = 5
    if(day == 6):
        return 0
    day += 1
    
    return day

def current_meal(day):
    current_time = datetime.time()
    print(current_time)
    weekday = day <= 5

    db_file_path = "homepage/static/DiningHallSchedules.sqlite"
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file_path)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    #execute a query to fetch data from a table
    if weekday == True:
        cursor.execute("SELECT * FROM DiningHallSchedules WHERE diningHallName = 'commons'")
    else:
        cursor.execute("SELECT * FROM DiningHallSchedules WHERE diningHallName = 'commons' AND weekDay = False")
    rows = cursor.fetchall()
    meal_times = {}
    for row in rows:
        print(row)

    # Close the cursor and connection when done
    cursor.close()
    conn.close()



def parse_html(request):
    # Open the existing HTML file
    with open('commons/templates/commons.html', 'r') as file:
        existing_html = file.read()

    # Check if the html file has already been parsed
    if '<hr class="dashed-line">' not in existing_html:
        # Perform the parsing and modification logic
        r = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall")
        html_content = r.content

        soup = BeautifulSoup(html_content, 'html.parser')

        br_lunch = br_lunch_day()
        dinner = dinner_day()
        current_date = datetime.date.today()
        day = current_date.weekday()
        current_meal(day)
        
        if day >= 5:
            
            
            soup2 = BeautifulSoup(existing_html, 'html.parser')
        
            target_elements = soup2.find_all('p', style = 'color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px')
        
            breakfast_tag = "BREAKFAST (7:00 - 9:30)"

            for tag in target_elements:
                if tag.text == breakfast_tag:
                    new_content = "BRUNCH (7:00 - 9:30)"  # Replace with your desired content
                    tag.string.replace_with(new_content)

            with open('commons/templates/commons.html', 'w') as file:
                file.write(str(soup2))
            
            with open('commons/templates/commons.html', 'r') as file:
                existing_html = file.read()
            
            brunch_day = 0
            
            if day == 6:
                brunch_day = 1
            
            existing_html = parse_meal(soup, 'accordion-block brunch', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">BRUNCH (7:00 - 9:30)</p>', brunch_day, existing_html)
            existing_html = parse_meal(soup, 'accordion-block dinner', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">DINNER (4:30 - 8:00)</p>', br_lunch, existing_html)
            
                
                    
        if day < 5:
            
            soup2 = BeautifulSoup(existing_html, 'html.parser')
        
            target_elements = soup2.find_all('p', style = 'color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px')
            
            breakfast_tag = "BRUNCH (7:00 - 9:30)"

            for tag in target_elements:
                if tag.text == breakfast_tag:
                    new_content = "BREAKFAST (7:00 - 9:30)"  # Replace with your desired content
                    tag.string.replace_with(new_content)

            with open('commons/templates/commons.html', 'w') as file:
                file.write(str(soup2))
            
            with open('commons/templates/commons.html', 'r') as file:
                existing_html = file.read()
                
            existing_html = parse_meal(soup, 'accordion-block breakfast', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">BREAKFAST (7:00 - 9:30)</p>', br_lunch, existing_html)
            existing_html = parse_meal(soup, 'accordion-block lunch', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">LUNCH (11:00 - 3:00)</p>', br_lunch, existing_html)
            existing_html = parse_meal(soup, 'accordion-block dinner', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">DINNER (4:30 - 8:00)</p>', dinner, existing_html)
            

        with open('commons/templates/commons.html', 'w') as file:
            file.write(existing_html)
            # Save the modified HTML
            
        # else:
        #     existing_html = parse_meal(soup, 'accordion-block breakfast', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 10px; margin-left: 68px; margin-bottom: 5px">BRUNCH (7:00 - 9:30)</p>', br_lunch, existing_html)
            
            
        
                
    return render(request, 'commons.html')



def parse_meal(soup, meal, html_pattern, day, existing_html):
    meal = meal.split(' ')[1]
    meal_type = soup.find_all('div', class_= meal)
    #meal_string = str(meal_type[day])
    
    if len(meal_type) > day:
        meal_string = str(meal_type[day])
    else:
        return existing_html
    
    meal_soup = BeautifulSoup(meal_string, 'html.parser')
    
    courses = meal_soup.find_all('div', class_='bite-menu-course')
    
    search_pattern = html_pattern
    index = existing_html.find(search_pattern)

    if index != -1:
        # Calculate the insertion index
        insertion_index = index + len(search_pattern)
        modified_html = existing_html[:insertion_index]

        for course in courses:
            station_name = course.find('h5').get_text(strip=True)
            modified_html += f'\n<button class="accordion">{station_name}</button>\n<div class="panel">\n'
            
            items = course.find_next_sibling('ul').find_all('li')
            
            for item in items:
                item_renamed = unidecode(str(item))
                item_name = re.search(r'data-fooditemname="([^"]+)"', item_renamed)
                
                calories = re.search(r'\d+cal', str(item))
                                     
                if item_name and calories:
                    item_name = item_name.group(1)
                    calories_group = calories.group()
                    match = re.search(r'\d+', calories_group)
                    cal = int(match.group())
                    
                    modified_html += f'\t\t<p style="font-size: 20px; margin-top: 20px; margin-left: 35px">{item_name} <button onclick = "addCalories({cal})" class = "button" data-calories = "{cal}" style = "color: red; border: none; font-size: 20px;">{calories.group()} </button></p>\n\t\t<hr class="dashed-line">\n'
            # Add rating system for the station
            station_name_slug = station_name.lower().replace(" ", "-")  # convert station name to lower case and replace spaces with hyphens
            rating_html = f'''
<p style="color: rgb(228, 30, 30); font-size: 19px; margin-top: 25px; margin-bottom: 10px; margin-right: 33px; text-align: right">RATE THIS STATION</p>
<div class="rating">
<input id="star5-{meal}-{station_name_slug}" name="rating-{meal}-{station_name_slug}" type="radio" value="5"/><label for="star5-{meal}-{station_name_slug}" title="Rocks!">5 stars</label>
<input id="star4-{meal}-{station_name_slug}" name="rating-{meal}-{station_name_slug}" type="radio" value="4"/><label for="star4-{meal}-{station_name_slug}" title="Pretty good">4 stars</label>
<input id="star3-{meal}-{station_name_slug}" name="rating-{meal}-{station_name_slug}" type="radio" value="3"/><label for="star3-{meal}-{station_name_slug}" title="Meh">3 stars</label>
<input id="star2-{meal}-{station_name_slug}" name="rating-{meal}-{station_name_slug}" type="radio" value="2"/><label for="star2-{meal}-{station_name_slug}" title="Kinda bad">2 stars</label>
<input id="star1-{meal}-{station_name_slug}" name="rating-{meal}-{station_name_slug}" type="radio" value="1"/><label for="star1-{meal}-{station_name_slug}" title="Sucks big time">1 star</label>
</div>
'''
            modified_html += rating_html

            modified_html += '\t\t</div>\n'
            
        modified_html += existing_html[insertion_index:]

        return modified_html

    else:
        # If the search_pattern is not found, return the existing_html as is
        return existing_html


 #remove the food items
def remove_items(request):
    
    with open('commons/templates/commons.html', 'r') as file:
        file_change = file.read()
    
    soup = BeautifulSoup(file_change, 'html.parser')
    
    headers = soup.find_all('p', style = 'color: rgb(228, 30, 30); font-size: 19px; margin-top: 25px; margin-bottom: 10px; margin-right: 33px; text-align: right')

    for header in headers:
        header.extract()

    buttons = soup.find_all('button', class_ = 'accordion')

    for button in buttons:
        button.extract()

    panels = soup.find_all('div', class_ = 'panel')

    for panel in panels:
        panel.extract()

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
    return render(request, 'commons/commons.html')

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
