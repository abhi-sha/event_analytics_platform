from sqlalchemy import Column,String,Integer,JSON
from sqlalchemy.orm import declarative_base

Base=declarative_base()


class Event(Base):

    __tablename__="events"

    event_id=Column(String,primary_key=True)
    event_name=Column(String)
    user_id=Column(String)
    timestamp=Column(Integer)
    properties=Column(JSON)
    