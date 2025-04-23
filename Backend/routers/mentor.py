from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.schemas import MentorRequest # type: ignore
from backend.database import get_db # type: ignore
from backend.utils.helpers import get_current_user # type: ignore
from backend.ai import mentor as mentor_ai # type: ignore
from backend.models import User as UserModel # type: ignore

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
        raise HTTPException(status_code=500, detail=str(e))
    
