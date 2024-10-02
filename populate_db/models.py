from django.db import models

class FoodItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(null=True)
    description = models.TextField(null=True)
    meal = models.TextField(null=True)
    station = models.TextField(null=True)
    dining_hall = models.TextField(null=True)

    
