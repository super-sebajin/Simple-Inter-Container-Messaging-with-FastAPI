from typing import Optional 
from pydantic import BaseModel, Field


class Message(BaseModel):
    payload: str = "Hello World"

   