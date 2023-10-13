from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Station(models.Model):
    name = models.CharField(max_length=200)

class Rating(models.Model):
    MEAL_TIMES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]

    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    meal_time = models.CharField(max_length=10, choices=MEAL_TIMES, default='dinner')