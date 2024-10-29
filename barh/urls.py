from django.urls import path
from . import views

urlpatterns = [

    path('', views.barh, name='barh'),
    path('rate/', views.rate, name='rate'),

]
