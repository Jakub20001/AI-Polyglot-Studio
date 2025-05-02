from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas import QuizQuestion 
from database import get_db
from models import User as UserModel 
from utils.helpers import get_current_user 
from AI import quiz as quiz_engine

router = APIRouter(
    prefix="/quiz",
    tags=["quiz"]
)

@router.post("/generate", response_model=List[QuizQuestion])
def generate_quiz(
    language: str,
    topic: str,
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return quiz_engine.generate_quiz(language=language, topic=topic)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
    
@router.post("/submit", response_model=List[QuizQuestion])
def submit_quiz(
    user_answers: List[QuizQuestion],
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        return quiz_engine.evaluate_answers(user_answers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
