from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.applicant = self.scope['url_route']['kwargs']['applicant']
        self.applicant_group_name = 'comment_%s' % self.applicant

        # Join room group
        await self.channel_layer.group_add(
            self.applicant_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.applicant_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        comment = text_data_json['comment']

        # Send message to room group
        await self.channel_layer.group_send(
            self.applicant_group_name,
            {
                'type': 'comment_message',
                'comment': comment,
            }
        )

    # Receive message from room group
    async def comment_message(self, event):
        comment = event['comment']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'comment': comment
        }))