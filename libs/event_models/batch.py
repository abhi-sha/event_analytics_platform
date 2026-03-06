from pydantic import BaseModel
from typing import List
from .event import Event


class EventBatch(BaseModel):
    events:List[Event]

