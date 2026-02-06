

from pydantic import BaseModel


class event(BaseModel):
    source: str | None = None
    eventType: str | None = None
    payload: str | None = None
    
class eventCreate(event):
    user_id:int
    device_id:int
    timestamp:str
    
class eventRead(event):
    id:int
    user_id:int
    device_id:int
    timestamp:str
    created_at:str
    
    class Config:
        orm_mode=True