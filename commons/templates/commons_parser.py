from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from bs4 import BeautifulSoup
import requests
import re



print("reached here yayyy")
    # Perform the parsing and modification logic
r = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall")
html_content = r.content

soup = BeautifulSoup(html_content, 'html.parser')
    
    #parsing_meal('accordion-block breakfast', soup)
    #parsing_meal('accordion-block lunch', soup)
breakfast = soup.find_all('div', class_='accordion-block breakfast')

with open("template.html", "r") as file:
    existing_html = file.read()

for i in breakfast:
        
    breakfast_string = str(i)
    pattern = r'data-fooditemname="([^"]+)"'
    result = re.findall(pattern, breakfast_string)

    if result:
        search_pattern = '<button class="accordion">Grill</button>\n    <div class="panel">\n'
        index = existing_html.find(search_pattern)

        if index != -1:
                # Calculate the insertion index
            insertion_index = index + len(search_pattern)
            modified_html = existing_html[:insertion_index]

            for item in result:
                modified_html += f'\t\t<p style="font-size: 24px; margin-top: 25px; margin-left: 30px">{item}</p>\n\t\t<hr class="dashed-line">\n'
                    #modified_html += f'<p style="font-size: 24px; margin-top: 25px; margin-left: 30px">ehekjekhederf</p>\n\t\t<hr class="dashed-line">= '

            modified_html += existing_html[insertion_index:]

            with open("commons.html", "w") as file:
                file.write(modified_html)