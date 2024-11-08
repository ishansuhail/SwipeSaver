"""
ASGI config for SwipeSaver project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SwipeSaver.settings')
django.setup()

from commons.urls import commons_websocket_urlpatterns
from blitman.urls import blitman_websocket_urlpatterns
from russellsage.urls import russelsage_websocket_urlpatterns
from barh.urls import barh_websocket_urlpatterns

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            commons_websocket_urlpatterns +
            blitman_websocket_urlpatterns +
            russelsage_websocket_urlpatterns +
            barh_websocket_urlpatterns
        )
    ),
})
