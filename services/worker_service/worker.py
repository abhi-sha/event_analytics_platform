import asyncio
import json

from libs.queue_client import RedisQueue
from libs.logging.logger import get_logger

logger=get_logger()


class Worker:

    def __init__(self,name="worker-1"):
        self.queue=RedisQueue()
        self.name=name
    
    async def start(self):

        await self.queue.create_consumer_group()

        logger.info("worker_started",worker=self.name)

        while True:

            events=await self.queue.read_events(self.name)

            if not events:
                continue
        
            for stream,message in events:

                for event_id,data in message:

                    event=json.loads(data[b"event"])

                    await self.process_event(event)

                    await self.queue.acknowledge_event(event_id)

    async def process_event(self,event):

        logger.info("event_processed",
                    event_name=event["event_name"],
                    user_id=event["user_id"])


