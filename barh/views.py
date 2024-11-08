# Django Imports
from django.shortcuts import render

# Local Application Imports
from populate_db.views import populate
from utils.rating_utils import submit_rating_util
from utils.dining_hall_utils import get_dining_hall_data

def barh(request):
    #populate(url = "https://rpi.sodexomyway.com/en-us/locations/barh-dining-hall", dining_hall = "barh")

    dining_hall = "barh"

    breakfast_items, lunch_items, dinner_items, brunch_items, ratings = get_dining_hall_data(request, dining_hall)

    # Pass the result to the template
    return render(request, dining_hall + '.html', {
        'dining_hall_name': dining_hall,
        'breakfast_items': breakfast_items,
        'brunch_items': brunch_items,
        'lunch_items': lunch_items,
        'dinner_items': dinner_items,
        'ratings': ratings,
        'is_authenticated': request.user.is_authenticated,
    })
 
def submit_rating(request):
    return submit_rating_util(request)