from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.schemas import DialogueRequest # type: ignore
from backend.utils.helpers import get_current_user # type: ignore
from backend.database import get_db # type: ignore
from backend.models import User as UserModel # type: ignore
from backend.ai import dialogue as dialogue_engine # type: ignore

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
        raise HTTPException(status_code=500, detail=str(e))