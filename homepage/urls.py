from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.home, name='homepage'),
    path('commons/', views.commons, name='commons'),
    path('barh/', views.barh, name='barh'),
    path('russellsage/', views.russellsage, name='russellsage'),
    path('blitman/', views.blitman, name='blitman'),

    # path('parse-html/', views.parse_html, name='parse_html'),
]
