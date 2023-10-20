from django.urls import path

from . import views
from contact import views_C
from about import views_A
from ratedfood import views_R

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.home, name='homepage'),
    path('commons/', views.commons, name='commons'),
    path('russellsage/', views.russellsage, name='russellsage'),
    path('contact/', views_C.contact, name='contact'),
    path('about/', views_A.about, name='about'),
    path('ratedfood/', views_R.ratedfood, name='ratedfood')

    # path('parse-html/', views.parse_html, name='parse_html'),
]
