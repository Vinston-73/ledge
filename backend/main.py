from fastapi import FastAPI
from dotenv import load_dotenv
 from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()


app.add_middleware(CORSMiddleware,
    allow_origins=["https://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

load_dotenv()


@app.get("/")
def read_root():
    return {"Hello": "World"}