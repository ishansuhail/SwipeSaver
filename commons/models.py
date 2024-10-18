from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


class Station(models.Model):
    name = models.CharField(max_length=200)

class Rating(models.Model):
    user_id = models.BigIntegerField(null=True)
    meal = models.TextField(null=True)
    station = models.TextField(null=True)
    dining_hall = models.TextField(null=True)
    rating = models.IntegerField(null=True)
