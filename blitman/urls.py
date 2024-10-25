from django.urls import path
from . import views

urlpatterns = [
    path('', views.blitman, name='blitman'),
    path('rate/', views.rate, name='rate'),
]