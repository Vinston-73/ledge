
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException,Request
from pydantic import BaseModel
from requests import Session
from schema.user import userCreate
from models.userModel import User
from models.event_daily import EventDaily
from database.db import Base, Engine, get_db
from routes.auth import router as auth_router 
from passlib.context import CryptContext
Base.metadata.create_all(bind=Engine)
app=FastAPI()
app.include_router(auth_router)

# @app.post("/ingest")
# async def ingest(event:dict):
#     sreqtime=datetime.now()
#     print("get the event",event)
#     ereqtime=datetime.now()
#     return {"status": "I got your event!", "event": event,"start_time":sreqtime,"end_time":ereqtime}

# # @app.post("/register   ")
# async def register(request:Request):
    
