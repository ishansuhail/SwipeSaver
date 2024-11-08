from django.urls import path
from . import views
from . import consumers
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.russellsage, name='russellsage'),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
]

russelsage_websocket_urlpatterns = [
    path("ws/log/russell-sage/", consumers.LogConsumer.as_asgi()),
]

