
from datetime import datetime
from fastapi import FastAPI,Request

app=FastAPI()

@app.get('/')
async def hello():
    return {"message": "Hello, World!"}

@app.post("/ingest")
async def ingest(event:dict):
    sreqtime=datetime.now()
    print("get the event",event)
    ereqtime=datetime.now()
    return {"status": "I got your event!", "event": event,"start_time":sreqtime,"end_time":ereqtime}