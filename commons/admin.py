from django.contrib import admin
from .models import Rating
from .models import testFoodItem

admin.site.register(Rating)
class RatedAdminTest(admin.ModelAdmin):
	list_display = ('food_name','image','rating','vegan','dining_hall','gluten_free','meal_time','callories' )
admin.site.register(testFoodItem,RatedAdminTest)
