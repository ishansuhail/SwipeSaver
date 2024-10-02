from django.shortcuts import render
from django.http import JsonResponse

import datetime

import requests
import json
import re
from bs4 import BeautifulSoup
from populate_db.models import FoodItem

# Create your views here.
def populate(url = "https://rpi.sodexomyway.com/en-us/locations/the-commons-dining-hall", dining_hall = "commons"):
    response = requests.get(url)
    html_content = response.text
    
    soup = BeautifulSoup(html_content, 'html.parser')
    script_tag = soup.find('script', text=re.compile(r'window\.__PRELOADED_STATE__'))
    if script_tag:
        script_content = script_tag.string
        split_content = script_content.split('window.__PRELOADED_STATE__ = ')
        
        if split_content:
            try: 
                json_data = json.loads(split_content[1].strip())  # Parse the JSON string into a Python dictionary
                data = json_data.get('composition').get('subject').get('regions')[1].get('fragments')[0].get('content').get('main').get('sections')
                
                # Extract info that we want
                for meal in data:
                    print(f"Meal: {meal.get('name')}")
                    for group in meal.get('groups', []):  # Ensure 'groups' is available
                        print(f"  Group name: {group.get('name')}")
                        for item in group.get('items', []):  # Ensure 'items' is available
                            
                            item_station = item.get('course')
                            item_meal = item.get('meal')
                            item_id = item.get('menuItemId')
                            item_name = item.get('formalName')
                            item_desc = item.get('description')
                            item_dining_hall = dining_hall

                            # Create a FoodItem instance
                            food_item = FoodItem(
                                id = item_id,
                                name=item_name,
                                description=item_desc,
                                meal=item_meal,
                                station=item_station,
                                dining_hall=item_dining_hall
                            )
                            
                            # Save the FoodItem instance to the database
                            food_item.save(using='PostgresDB')
                            

                #print(json.dumps(data, indent=4))
            except json.JSONDecodeError as e:
                print("Error decoding JSON:", e)  # Part after the delimiter

def food_item_list(request):
    # Fetch all food items
    food_items = FoodItem.objects.all().values('id', 'name', 'description', 'station', 'dining_hall', 'meal')
    
    # Convert to list
    food_items_list = list(food_items)
    
    return JsonResponse(food_items_list, safe=False)

    
