from pydantic import BaseModel

class userBase(BaseModel):
    name:str
    email:str
    
class userCreate(userBase):
    password:str
    

class userRead(userBase):
    id:int
    created_at:str
    last_used:str
    is_active:bool
    
    class Config:
        from_attributes = True