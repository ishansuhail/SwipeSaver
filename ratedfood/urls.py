from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ratedfood/', views.ratedfood, name='ratedfood')
]
