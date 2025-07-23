from channels.generic.websocket import AsyncWebsocketConsumer
import json

# chat/consumers.py
class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope["url_route"]["kwargs"]["id_user"]
        self.group_name = f"user_{self.user_id}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"],
            "from_user": event["from_user"],
            "date": event["date"]
        }))
