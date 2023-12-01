from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


class Station(models.Model):
    name = models.CharField(max_length=200)

class Rating(models.Model):
    MEAL_TIMES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    date = models.DateField(default=datetime.date.today)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    meal_time = models.CharField(max_length=10, choices=MEAL_TIMES, default='dinner')

class testFoodItem(models.Model):
    food_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='ratedfood_images/', blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places = 1)
    vegan = models.BooleanField()
    dining_hall = models.CharField(max_length=50, default = 'commons')
    meal_time = models.CharField(max_length=50, default = 'breakfast')
    gluten_free = models.BooleanField(default = False)
    callories = models.DecimalField(max_digits=4, decimal_places=0, default=0)
