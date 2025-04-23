from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.schemas import QuizQuestion # type: ignore
from backend.database import get_db # type: ignore
from backend.models import User as UserModel # type: ignore
from backend.utils.helpers import get_current_user # type: ignore
from backend.ai import quiz as quiz_engine # type: ignore

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
        questions = quiz_engine.generate_quiz(language=language, topic=topic)
        return questions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/submit", response_model=List[QuizQuestion])
def submit_quiz(
    user_answers: List[QuizQuestion],
    current_user: UserModel = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    try:
        results = quiz_engine.evaluate_answers(user_answers)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))