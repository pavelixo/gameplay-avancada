from django.urls import re_path
from .consumers import HealthCheckConsumer

websocket_urlpatterns = [
  re_path(r'ws/health_check/$', HealthCheckConsumer.as_asgi()),
]