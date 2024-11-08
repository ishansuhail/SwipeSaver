from django.urls import path
from . import views
from . import consumers
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.barh, name='barh'),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
]

barh_websocket_urlpatterns = [
    path("ws/log/barh/", consumers.LogConsumer.as_asgi()),
]