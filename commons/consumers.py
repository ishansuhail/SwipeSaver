import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Avg
from .models import Rating  # Assume you have a Rating model with a 'score' field
from channels.db import database_sync_to_async
import asyncio

class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Start the background task to continuously calculate and send averages
        self.loop_task = asyncio.create_task(self.send_average_ratings_per_station())

    async def disconnect(self, close_code):
        # Cancel the background task on disconnect
        if hasattr(self, 'loop_task'):
            self.loop_task.cancel()

    async def send_average_ratings_per_station(self):
        while True:
            await asyncio.sleep(5)  # Send updates every 5 seconds
            avg_ratings = await self.get_average_ratings_per_station()
            await self.send(text_data=json.dumps({"average_ratings": avg_ratings}))

    async def get_average_ratings_per_station(self):
        try:
            avg_ratings = await database_sync_to_async(
                lambda: list(
                    Rating.objects.filter(dining_hall="commons")
                                  .values('meal', 'station')
                                  .annotate(average_rating=Avg('rating'))
                                  .order_by('meal', 'station')
                )
            )()
        except Exception as e:
            print(f"Error fetching average ratings per station: {e}")
            return []
        
        # Format the data
        return [
            {
                "meal": result['meal'],
                "station": result['station'], 
                "average_rating": result['average_rating'] or 0}
            for result in avg_ratings
        ]