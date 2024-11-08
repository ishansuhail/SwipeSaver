from django.urls import path
from . import views
from . import consumers
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.commons, name='commons'),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
]

commons_websocket_urlpatterns = [
    path("ws/log/commons/", consumers.LogConsumer.as_asgi()),
]
