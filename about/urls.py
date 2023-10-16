from django.urls import path

from . import views_A

urlpatterns = [
    path('', views_A.home, name='home'),
]