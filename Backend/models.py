from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    xp = Column(Integer, default=0)
    
    quizzes = relationship("QuizResult", back_populates="user")
    dialogs = relationship("Dialog", back_populates="User")
    feedbacks = relationship("MentorFeedback", back_populates="user")
    
class QuizResult(Base):
    __tablename__ = "quiz_results"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    language = Column(String)
    score = Column(Integer)
    date_taken = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="quizzes")
    
class Dialog(Base):
    __tablename__ = "dialogs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    topic = Column(String)
    user_input = Column(Text)
    ai_response = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="dialogs")
    