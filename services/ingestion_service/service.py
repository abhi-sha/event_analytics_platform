from libs.event_models import EventBatch
from libs.logging.logger import get_logger
from libs.queue_client import RedisQueue


logger=get_logger()


class IngestionService:

    def __init__(self):
        self.queue=RedisQueue()


    async def ingest(self,batch:EventBatch):

        event_count=len(batch.events)

        for event in batch.events:
            await self.queue.publish_event(event.model_dump())

        logger.info("" \
        "events_received",
        count=event_count)


        return{
            "status":"accepted",
            "events_received":event_count
        }