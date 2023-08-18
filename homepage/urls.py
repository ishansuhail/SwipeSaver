from django.urls import path

from . import views
from contact import views_C
from about import views_A

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.home, name='homepage'),
    path('commons/', views.commons, name='commons'),
    path('contact/', views_C.contact, name='contact'),
    path('about/', views_A.about, name='about'),
    path('ratedfood/', views.ratedfood, name='ratedfood')
]
