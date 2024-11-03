from celery import shared_task
from .models import FoodItem
from .views import populate
from populate_db.models import Rating

@shared_task
def update_food_items():
        
    # Delete information from tables
    FoodItem.objects.all().delete()
    Rating.objects.all().delete()
    
    # List of urls to scrape from
    urls = [
        'https://rpi.sodexomyway.com/en-us/locations/the-commons-dining-hall',
        'https://rpi.sodexomyway.com/en-us/locations/russell-sage-dining-hall',
        'https://rpi.sodexomyway.com/en-us/locations/barh-dining-hall',
        'https://rpi.sodexomyway.com/en-us/locations/blitman-dining-hall']
    
    # Dining hall strings
    dining_halls = ["commons", "sage", "barh", "blitman"]
    
    # Scrape all the data and store it in the database
    for url, dining_hall in zip(urls, dining_halls):
        populate(url, dining_hall)
