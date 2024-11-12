from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
from utils.rating_utils import send_average_ratings_per_station

class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        hall_name = "russell-sage"
        self.loop_task = asyncio.create_task(send_average_ratings_per_station(self, hall_name))

    async def disconnect(self, close_code):
        if hasattr(self, 'loop_task'):
            self.loop_task.cancel()
