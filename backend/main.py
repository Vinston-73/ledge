
from datetime import datetime
from fastapi import FastAPI,Request
from models.event_daily import EventDaily
from database.db import Base, Engine

Base.metadata.create_all(bind=Engine)
app=FastAPI()

@app.get('/')
async def hello():
    return {"message": "Hello, World!"}

# @app.post("/ingest")
# async def ingest(event:dict):
#     sreqtime=datetime.now()
#     print("get the event",event)
#     ereqtime=datetime.now()
#     return {"status": "I got your event!", "event": event,"start_time":sreqtime,"end_time":ereqtime}

# # @app.post("/register   ")
# async def register(request:Request):
    