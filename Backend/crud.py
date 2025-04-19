from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username = user.username, email = user.email, hashed_password = hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_xp(db: Session, user_id: int):
    return db.query(models.XP).filter(models.XP.user_id == user_id).first()
        
def update_user_xp(db: Session, user_id: int, xp_gain: int):
    xp_entry = get_user_xp(db, user_id)
    if xp_entry:
        xp_entry.points += xp_gain
    else:
        xp_entry = models.XP(user_id=user_id, points=xp_gain)
        db.add(xp_entry)
    db.commit()
    db.refresh(xp_entry)
    return xp_entry