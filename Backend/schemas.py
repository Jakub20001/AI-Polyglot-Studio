from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class XP(BaseModel):
    user_id: int
    points: int
    
class DialogueRequest(BaseModel):
    topic: str
    level: str
    
class QuizQuestion(BaseModel):
    question: str
    correct_answer: str
    user_answer: Optional[str]
    is_correct: Optional[bool] = False
    
class MentorRequest(BaseModel):
    language: str
    query: str
    
    