from typing import Optional 
from pydantic import BaseModel, Field


class Message(BaseModel):
    payload: str = None
    hostname: str = None
    port: str = None
   