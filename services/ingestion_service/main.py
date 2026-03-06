from fastapi import FastAPI
from libs.event_models import EventBatch
from libs.logging.logger import configure_logging
from .middleware import RequestIDMiddleware
from .service import IngestionService

configure_logging()

app=FastAPI(title="Event Ingestion Service")
app.add_middleware(RequestIDMiddleware)
service=IngestionService()


@app.get("/health")
async def health_check():
    return {"status":"ok"}


@app.post("/events")
async def ingest_events(batch:EventBatch):

    result=await service.ingest(batch)
    return result