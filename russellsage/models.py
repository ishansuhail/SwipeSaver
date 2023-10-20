from django.db import models
<<<<<<< HEAD
=======
import datetime
>>>>>>> 382fd638787ec15e98cfcdd54181c22b7b7badf3
from django.core.validators import MinValueValidator, MaxValueValidator


class Station(models.Model):
    name = models.CharField(max_length=200)

class Rating(models.Model):
    MEAL_TIMES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
<<<<<<< HEAD

=======
    date = models.DateField(default=datetime.date.today)
>>>>>>> 382fd638787ec15e98cfcdd54181c22b7b7badf3
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    meal_time = models.CharField(max_length=10, choices=MEAL_TIMES, default='dinner')
