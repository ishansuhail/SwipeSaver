from django.contrib import admin
from .models import FoodItem
from .models import Rating

# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Rating)
