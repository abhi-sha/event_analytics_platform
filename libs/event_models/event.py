from pydantic import BaseModel,Field
from typing import Dict,Any
from enum import Enum

class EventName(str,Enum):
    page_view="page_view"
    signup="signup"
    login="login"
    purchase="purchase"
    api_call="api_call"
    error_event="error_event"

class Event(BaseModel):
    event_id:str=Field(...,description="unique event identifier")
    event_name:EventName
    user_id:str
    timestamp:int
    properties:Dict[str,Any]={}

    class Config:
        schema_extra={
            "example":{
                "event_id": "evt_123",
                "event_name": "page_view",
                "user_id": "user_42",
                "timestamp": 1710000000,
                "properties": {
                    "page": "/home",
                    "device": "mobile"
            }}
        }