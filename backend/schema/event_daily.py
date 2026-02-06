from pydantic import BaseModel

class EventDaily(BaseModel):
    date: str
    event_count: int
    
class EventDailyCreate(EventDaily):
    user_id:int
    device_id:int
    event_type:str
    
class EventDailyRead(EventDaily):
    id:int
    user_id:int
    device_id:int
    event_type:str
    
    class Config:
        orm_mode=True