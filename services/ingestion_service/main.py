from fastapi import FastAPI

app=FastAPI(title="Event Ingestion Service")


@app.get("/health")
async def health_check():
    return {"status":"ok"}