from pydantic import BaseModel
from typing import Any, Dict

class ChatRequest(BaseModel):
    query: str
    chatty: bool = False

class ChatResponse(BaseModel):
    message: Dict[str, Any]
