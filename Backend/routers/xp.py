from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Backend import crud 
from database import get_db 
from schemas import XP 
from utils.helpers import get_current_user 
from models import User as UserModel 

router = APIRouter(
    prefix="/xp",
    tags=["xp"]
)

@router.get("/", response_model=XP)
def get_user_xp(current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    xp = crud.get_user_xp(db, user_id = current_user.id)
    if xp is None:
        raise HTTPException(status_code=404, detail="XP not found for user")
    return xp

@router.post("/gain", response_model=XP)
def gain_xp(points: int, current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    if points <= 0:
        raise HTTPException(status_code=400, detail="Points must be a positive integer.")
    return crud.update_user_xp(db, user_id = current_user.id, xp_gain = points)
