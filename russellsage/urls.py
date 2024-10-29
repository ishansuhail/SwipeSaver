from django.urls import path
from . import views

urlpatterns = [

    path('', views.russellsage, name='russellsage'),
    path('rate/', views.rate, name='rate'),

]
