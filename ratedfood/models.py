from django.db import models

# Create your models here.


class ratedFoodItem(models.Model):
	food_name = models.CharField(max_length=50)
	image = models.CharField(max_length=50)
	rating = models.DecimalField(max_digits=2, decimal_places = 1)
	vegan = models.BooleanField()

	