from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ratedFoodItem

class RatedAdmin(admin.ModelAdmin):
	list_display = ('food_name','image','rating','vegan','dining_hall','gluten_free','meal_time' )
admin.site.register(ratedFoodItem,RatedAdmin)