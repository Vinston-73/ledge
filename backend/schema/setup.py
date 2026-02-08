from pydantic import BaseModel

class Setup(BaseModel):
    code:str
    verification_code:str
    nickname:str
    
class SetupCreate(Setup):
    expires_at:str
    user_id:int
    

class SetupRead(Setup):
    id:int
    created_at:str
    expires_at:str
    is_used:bool
    user_id:int
    class Config:
        orm_mode=True