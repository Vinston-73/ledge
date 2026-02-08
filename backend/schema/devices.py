from pydantic import BaseModel

class Device(BaseModel):
    username: str
    device_name:str
    email:str
    device_token:str

    
class DeviceCreate(BaseModel):
    user_id: int
    
    
class DeviceRead(Device):
    id: int
    user_id: int
    created_at: str
    is_active: bool
    last_used: str
    
    class Config:
        from_attributes = True