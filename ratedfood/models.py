from django.db import models

# Create your models here.


class ratedFoodItem(models.Model):
	food_name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='ratedfood_images/', blank=True, null=True)
	rating = models.DecimalField(max_digits=2, decimal_places = 1)
	vegan = models.BooleanField()
	dining_hall = models.CharField(max_length=50, default = 'commons')
	gluten_free = models.BooleanField(default = False)

	#TO ADD NEW FOOD ITEM TO DATABASE REFER TO VIEWS_R.PY / def addRatedFoodItem(request): / URL: http://127.0.0.1:8000/add_rated_food_item/

	