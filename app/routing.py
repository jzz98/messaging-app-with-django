from django.urls import path
from chats.consumers import UserConsumer

websocket_urlpatterns = [
    path("ws/chat/dialog/<int:id_user>", UserConsumer.as_asgi()),
]
