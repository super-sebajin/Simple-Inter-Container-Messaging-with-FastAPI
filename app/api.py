from fastapi import FastAPI, HTTPException
from .message import Message


app = FastAPI()

@app.get("/")
async def root():
    return {"greetings": "hello world!"}

@app.post("/message/")
async def message(msg: Message):
    if msg is None:
        raise HTTPException(status_code=400,detail="Payload empty")
    
    return msg


    