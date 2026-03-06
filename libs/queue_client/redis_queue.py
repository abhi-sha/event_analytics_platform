import json
import redis.asyncio as redis

STREAM_NAME="events_stream"


class RedisQueue:

    def __init__(self,host="localhost",port=6379):

        self.redis=redis.Redis(host=host,port=port)

    async def publish_event(self,event:dict):
        
        await self.redis.xadd(
            STREAM_NAME,
            {"event":json.dumps(event)}
        )
        