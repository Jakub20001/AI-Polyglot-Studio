from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import MentorRequest 
from database import get_db 
from utils.helpers import get_current_user
from AI import mentor as mentor_ai 
from models import User as UserModel 

router = APIRouter(
    prefix="/mentor",
    tags=["mentor"]
)

@router.post("/ask")
def ask_mentor(
    request: MentorRequest,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        response = mentor_ai.get_mentor_response(request.language, request.query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
    
