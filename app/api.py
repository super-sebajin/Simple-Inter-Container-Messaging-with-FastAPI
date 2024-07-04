from fastapi import FastAPI, HTTPException
from .message import Message
import requests
import os
import socket 
from dotenv import load_dotenv

load_dotenv()

hostname = socket.gethostname()

app = FastAPI()

@app.get("/")
async def root():
    return {"greetings": "hello world!"}

@app.post("/message/")
async def message(msg: Message):
    if msg is None:
        raise HTTPException(status_code=400,detail="Payload empty")
    try:
        if msg.payload == "get-root" and os.getenv(msg.hostname) != hostname:
            
            url = f"http://{os.getenv(msg.hostname)}:{os.getenv(msg.port)}"
            request = requests.get(url)
            return request.json()
    except:
        return msg



    