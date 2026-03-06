from libs.event_models import EventBatch
from libs.logging.logger import get_logger

logger=get_logger()


class IngestionService:


    async def ingest(self,batch:EventBatch):

        event_count=len(batch.events)


        logger.info("" \
        "events_received",
        count=event_count)


        return{
            "status":"accepted",
            "events_received":event_count
        }