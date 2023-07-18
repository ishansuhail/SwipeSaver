from django.shortcuts import render

import datetime

from django.http import JsonResponse
from django.db.models import Avg
# Create your views here.
from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests
import re

def parse_meal(soup, meal, html_pattern):
    meal_type = soup.find_all('div', class_= meal)

    with open('commons.html', "r") as file:
        existing_html = file.read()

    current_date = datetime.date.today()
    day_ = current_date.weekday()
    
    count = 0
    for i in meal_type:
        
        meal_string = str(i)
        pattern = r'data-fooditemname="([^"]+)"'
        result = re.findall(pattern, meal_string)

        if result:

            
            
            search_pattern = html_pattern + '\n<button class="accordion">Grill</button>\n<div class="panel">\n'
            index = existing_html.find(search_pattern)


            print(index)

            if index != -1:
                print("reached all food")
                # Calculate the insertion index
                insertion_index = index + len(search_pattern)
                modified_html = existing_html[:insertion_index]

                for item in result:
                    modified_html += f'\t\t<p style="font-size: 24px; margin-top: 25px; margin-left: 30px">{item}</p>\n\t\t<hr class="dashed-line">\n'
                    #modified_html += f'<p style="font-size: 24px; margin-top: 25px; margin-left: 30px">ehekjekhederf</p>\n\t\t<hr class="dashed-line">= '

                modified_html += existing_html[insertion_index:]

                with open("commons.html", "w") as file:
                    file.write(modified_html)
        count += 1
    
    
with open('commons.html', 'r') as file:
    existing_html = file.read()
#if '<hr class="dashed-line">' in existing_html:
    #print('kekeke')
    
    # Perform the parsing and modification logic
r = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall")
html_content = r.content

soup = BeautifulSoup(html_content, 'html.parser')
    
    
parse_meal(soup, 'accordion-block breakfast', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 10px; margin-left: 68px; margin-bottom: 5px">BREAKFAST (7:00 - 9:30)</p>')
#parse_meal(soup, 'accordion-block lunch', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px;margin-bottom: 5px">LUNCH (11:00 - 3:00)</p>')
#parse_meal(soup, 'accordion-block dinner', '<p style="color: rgb(228, 30, 30); font-size: 32px; margin-top: 35px; margin-left: 68px; margin-bottom: 5px">DINNER (4:30 - 8:00)</p>')

    

