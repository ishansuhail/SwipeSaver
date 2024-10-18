from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.commons, name='commons'),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
]
