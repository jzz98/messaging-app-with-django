from django.urls import re_path
from chats import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/dialog/(?P<id_user>\d+)$', consumers.ChatConsumer.as_asgi()),
]
