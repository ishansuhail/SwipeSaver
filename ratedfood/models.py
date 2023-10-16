from django.db import models

# Create your models here.


class ratedFoodItem(models.Model):
	food_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='ratedfood_images/', blank=True, null=True)
	rating = models.DecimalField(max_digits=2, decimal_places = 1)
	vegan = models.BooleanField()
	dining_hall = models.CharField(max_length=50, default = 'commons')

	