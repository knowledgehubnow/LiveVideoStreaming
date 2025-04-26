import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
from stream.models import LiveStream
from asgiref.sync import sync_to_async

class StreamConsumer(AsyncWebsocketConsumer):
    viewers = 0

    async def connect(self):
        # Parse query string to get 'room'
        query_string = self.scope['query_string'].decode()
        query_params = parse_qs(query_string)
        room = query_params.get('room', [None])[0]
        print(room, "Received room in connect")

        if room is None:
            await self.close()
            return

        self.room_name = room
        self.room_group_name = f"live_stream_{room}"

        await self.accept()

        # Join group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Increase viewer count
        StreamConsumer.viewers += 1

        # Broadcast updated viewer count
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "update_viewers",
                "count": StreamConsumer.viewers
            }
        )

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

        StreamConsumer.viewers -= 1

        # Set the stream's is_streaming to False if viewers == 0
        if StreamConsumer.viewers <= 0:
            try:
                await self.set_stream_off(self.room_name)
            except Exception as e:
                print("Error updating is_streaming on disconnect:", e)

    @sync_to_async
    def set_stream_off(self, room):
        stream = LiveStream.objects.filter(room=room).first()
        if stream:
            stream.is_streaming = False
            stream.save()

    async def receive(self, text_data):
        print("Received message:", text_data)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'broadcast',
                'message': text_data
            }
        )

    async def broadcast(self, event):
        await self.send(text_data=event['message'])

    async def update_viewers(self, event):
        await self.send(text_data=json.dumps({
            'type': 'viewer_count',
            'count': event['count']
        }))
