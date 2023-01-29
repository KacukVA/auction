from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r"ws/lot/(?P<lot_id>\d+)/$", consumers.LotConsumer.as_asgi())
]