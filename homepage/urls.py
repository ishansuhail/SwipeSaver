from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('homepage/', views.home, name='homepage'),
    path('commons/', views.commons, name='commons'),
    path('russellsage/', views.russellsage, name='russellsage'),
<<<<<<< HEAD
    path('blitman/', views.blitman, name='blitman'),
=======
>>>>>>> 382fd638787ec15e98cfcdd54181c22b7b7badf3

    # path('parse-html/', views.parse_html, name='parse_html'),
]
