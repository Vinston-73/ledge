from pydantic import BaseModel

class event(BaseModel):
    source:str
    event_type:str
    payload:str

    
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
        from_attributes = True