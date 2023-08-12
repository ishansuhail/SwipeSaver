from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ratedfood/', views.ratedfood, name='display_FOOD'),
    path('display_FOOD/', views.display_FOOD, name='display_FOOD')
]
