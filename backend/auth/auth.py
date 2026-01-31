from datetime import datetime, timedelta
import os
import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv



load_dotenv()
Secret_key=os.getenv("SECRET_KEY")
ALGORITHM="HS256"

pwd_context=CryptContext(schemas=["bcrypt"],deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire=datetime.now()+(expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode,Secret_key,algorithm=ALGORITHM)