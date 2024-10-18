# Standard Library Imports
import datetime
import re
import json

# Third-Party Library Imports
from unidecode import unidecode

# Django Imports
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg

# Local Application Imports
from populate_db.views import populate
from populate_db.models import FoodItem
from .models import Rating, Station

from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

def commons(request):
    #populate(url = "https://rpi.sodexomyway.com/en-us/locations/the-commons-dining-hall")

    breakfast_items = FoodItem.objects.filter(dining_hall="commons", meal='BREAKFAST').order_by('station', 'name')
    lunch_items = FoodItem.objects.filter(dining_hall="commons", meal='LUNCH').order_by('station', 'name')
    dinner_items = FoodItem.objects.filter(dining_hall="commons", meal='DINNER').order_by('station', 'name')
    
    user_id = request.user.id
    ratings = Rating.objects.filter(dining_hall="commons", user_id=user_id)
    
    # Pass the result to the template
    return render(request, 'commons.html', {'breakfast_items': breakfast_items, 'lunch_items': lunch_items, 'dinner_items': dinner_items, 'ratings': ratings})
 
@login_required
@require_POST  
def submit_rating(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return JsonResponse({'message': 'You must be logged in to submit a rating.', 'success': False}, status=401)
    
    try:
        data = json.loads(request.body)  # Parse the JSON data
        rating = data.get('rating')
        station = data.get('station')
        dining_hall = data.get('dining_hall')
        meal = data.get('meal')
        user_id = request.user.id

        # Validate input data
        if rating not in [1, 2, 3, 4, 5]:
            return JsonResponse({'message': 'Invalid rating value.', 'success': False}, status=400)

        if not station or not dining_hall:
            return JsonResponse({'message': 'Station and dining hall are required.', 'success': False}, status=400)

        # Check if the user has already rated this station
        existing_rating = Rating.objects.filter(user_id=user_id, station=station, dining_hall=dining_hall, meal=meal).first()

        if existing_rating:
            existing_rating.rating = rating
            existing_rating.save()  # Update the existing rating
        else:
            Rating.objects.create(user_id=user_id, station=station, rating=rating, dining_hall=dining_hall, meal=meal)  # Create a new rating

        return JsonResponse({'message': 'Rating submitted successfully!', 'success': True})
    
    except json.JSONDecodeError:
        return JsonResponse({'message': 'Invalid JSON format.', 'success': False}, status=400)
    except Exception as e:
        # Consider logging the error
        return JsonResponse({'message': str(e), 'success': False}, status=400)


