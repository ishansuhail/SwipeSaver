from django.urls import path
from . import views

urlpatterns = [
    path('', views.commons, name='commons'),
    path('rate/', views.rate, name='rate'),
]
