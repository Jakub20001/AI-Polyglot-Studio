from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import DialogueRequest 
from utils.helpers import get_current_user 
from database import get_db 
from models import User as UserModel 
from AI import dialogue as dialogue_engine 

router = APIRouter(
    prefix="/dialogue",
    tags=["dialogue"]
)

@router.post("/generate")
def generate_dialogue(
    request: DialogueRequest,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        generated = dialogue_engine.generate_dialogue(topic=request.topic, level=request.level)
        return {"user": current_user.username, "dialogue": generated}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
