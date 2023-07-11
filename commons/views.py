from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg
from .models import Rating, Station

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to SwipeSaver!")

def commons(request):
    return HttpResponse("Welcome to Commons!")

def rate(request):
    if request.is_ajax():
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

