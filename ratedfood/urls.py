from django.urls import path

from . import views_R

urlpatterns = [
    path('', views_R.home, name='home'),
    path('ratedfood/', views_R.ratedfood, name='display_FOOD'),
    path('display_FOOD/', views_R.display_FOOD, name='display_FOOD'),
    path('ratedfood_low/', views_R.ratedfood_low, name='ratedfood_low'),
    path('ratedfood_high/', views_R.ratedfood_high, name='dratedfood_high'),
    path('ratedfood_vegan/', views_R.ratedfood_vegan, name='ratedfood_vegan'),

]
