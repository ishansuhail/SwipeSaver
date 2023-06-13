from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.home, name='homepage'),
    path('commons/', views.commons, name='commons'),
    path('contact/',views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
