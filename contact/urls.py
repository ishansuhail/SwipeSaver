from django.urls import path

from . import views_C

urlpatterns = [
    path('', views_C.home, name='home'),
]