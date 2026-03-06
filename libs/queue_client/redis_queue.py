import json
import redis.asyncio as redis

STREAM_NAME="events_stream"
GROUP_NAME="event_workers"


class RedisQueue:

    def __init__(self,host="localhost",port=6379):

        self.redis=redis.Redis(host=host,port=port)

    async def publish_event(self,event:dict):
        
        await self.redis.xadd(
            STREAM_NAME,
            {"event":json.dumps(event)}
        )

    async def create_consumer_group(self):
        try:
            await self.redis.xgroup_create(
                STREAM_NAME,
                GROUP_NAME,
                id="0",
                mkstream=True
            )
        except Exception:
            pass 
    
    async def read_events(self,consumer_name):

        events=await self.redis.xreadgroup(
            GROUP_NAME,
            consumer_name,
            streams={STREAM_NAME:">"},
            count=10,
            block=5000
        )

        return events
    
    async def acknowledge_event(self,event_id):
        await self.redis.xack(STREAM_NAME,GROUP_NAME,event_id)

        