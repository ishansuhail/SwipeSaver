# accounts/urls.py
from django.urls import path
from .views import signup_view, login_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]
