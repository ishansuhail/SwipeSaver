from populate_db.models import FoodItem, Rating

# Function used to fetch all of the dining hall information for a page
def get_dining_hall_data(request, hall_name):
    breakfast_items = FoodItem.objects.filter(dining_hall=hall_name, meal='BREAKFAST').order_by('station', 'name')
    lunch_items = FoodItem.objects.filter(dining_hall=hall_name, meal='LUNCH').order_by('station', 'name')
    dinner_items = FoodItem.objects.filter(dining_hall=hall_name, meal='DINNER').order_by('station', 'name')
    brunch_items = FoodItem.objects.filter(dining_hall=hall_name, meal="BRUNCH").order_by('station', 'name')   

    user_id = request.COOKIES.get('user_id')
    ratings = Rating.objects.filter(dining_hall=hall_name, user_id=user_id)
    
    return breakfast_items, lunch_items, dinner_items, brunch_items, ratings