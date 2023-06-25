import requests
from bs4 import BeautifulSoup

r = requests.get("https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rpi.sodexomyway.com/dining-near-me/commons-dining-hall")

html_content = r.content

soup = BeautifulSoup(html_content, 'html.parser')

elements = soup.find_all('a', class_='get-nutritioncalculator', attrs={'data-fooditemname': True})

# Iterate over the elements and extract information
for element in elements:
    href = element['href']
    role = element['role']
    aria_describedby = element['aria-describedby']
    item_id = element['id']
    class_name = element['class']
    food_item_name = element['data-fooditemname']
    number = element['data-number']
    food_item_id = element['data-fooditemid']
    text = element.text
    
    # Do something with the extracted information
    print('Href:', href)
    print('Role:', role)
    print('Aria Describedby:', aria_describedby)
    print('Item ID:', item_id)
    print('Class:', class_name)
    print('Food Item Name:', food_item_name)
    print('Number:', number)
    print('Food Item ID:', food_item_id)
    print('Text:', text)
    print('---')







