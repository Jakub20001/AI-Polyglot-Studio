from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Message(BaseModel):
    user_input: str
    language: str

@router.post("/chat")
def chat_with_ai(msg: Message):
    return {"response": f"Simulated response in {msg.language}: {msg.user_input[::-1]}"}
