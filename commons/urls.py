from django.urls import path

from . import views

urlpatterns = [
    path('parse-html/', views.parse_html, name='parse_html'),
    path('commons/', views.commons, name='commons'), 
]
