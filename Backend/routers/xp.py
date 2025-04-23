from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend import crud
from backend.database import get_db # type: ignore
from backend.schemas import XP # type: ignore
from backend.utils.helpers import get_current_user # type: ignore
from backend.models import User as UserModel # type: ignore

router = APIRouter(
    prefix="/xp",
    tags=["xp"]
)

@router.get("/", response_model=XP)
def get_user_xp(current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    xp = crud.get_user_xp(db, user_id = current_user.id)
    if not xp:
        raise HTTPException(status_code=404, detail="XP not found for user")
    return xp

@router.post("/gain", response_model=XP)
def gain_xp(points: int, current_user: UserModel = Depends(get_current_user), db: Session = Depends(get_db)):
    updated_xp = crud.update_user_xp(db, user_id=current_user.id, xp_gain=points)
    return updated_xp