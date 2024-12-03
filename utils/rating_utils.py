import json
import asyncio

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Avg
from channels.db import database_sync_to_async
from populate_db.models import Rating

# Function used to submit user ratings to the database
@require_POST  
def submit_rating_util(request):
    # Check if the user_id cookie exists
    user_id = request.COOKIES.get('user_id')
    if not user_id:
        return JsonResponse({'message': 'User ID cookie is missing.', 'success': False}, status=400)
    
    try:
        data = json.loads(request.body)  # Parse the JSON data
        rating = data.get('rating')
        station = data.get('station')
        dining_hall = data.get('dining_hall')
        meal = data.get('meal')

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
    
# Funcion used to fetch the average ratings per station
async def get_average_ratings_per_station(hall_name):
    try:
        avg_ratings = await database_sync_to_async(
            lambda: list(
                Rating.objects.filter(dining_hall=hall_name)
                                .values('meal', 'station')
                                .annotate(average_rating=Avg('rating'))
                                .order_by('meal', 'station')
            )
        )()
    except Exception as e:
        print(f"Error fetching average ratings per station: {e}")
        return []

    # Format the data
    return [
        {
            "meal": result['meal'],
            "station": result['station'], 
            "average_rating": result['average_rating'] or 0}
        for result in avg_ratings
    ]

# Function used to fetch the average ratings for each station every 5 seconds
async def send_average_ratings_per_station(self, hall_name):
    while True:
        await asyncio.sleep(5)
        avg_ratings = await get_average_ratings_per_station(hall_name)
        await self.send(text_data=json.dumps({"average_ratings": avg_ratings}))