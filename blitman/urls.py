from django.urls import path
from . import views
from . import consumers
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.blitman, name='blitman'),
    path('submit-rating/', views.submit_rating, name='submit_rating'),
]

blitman_websocket_urlpatterns = [
    path("ws/log/blitman/", consumers.LogConsumer.as_asgi()),
]