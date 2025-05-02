from sqlalchemy.orm import Session
from collections import defaultdict
from typing import Dict, Any
from models import User, XP, QuizAnswer, DialogueLog, MentorInteraction

def count_total_users(db: Session) -> int:
    return db.query(User).count()

def total_xp_earned(db: Session) -> int:
    return db.query(XP).with_entities(XP.points).all() and sum(x[0] for x in db.query(XP.points).all())

def get_user_quiz_stats(db: Session, user_id: int) -> Dict[str, Any]:
    attempts = db.query(QuizAnswer).filter(QuizAnswer.user_id == user_id).all()
    total = len(attempts)
    correct = len([a for a in attempts if a.is_correct])
    return {
        "total_attempts": total,
        "correct_answers": correct,
        "accuracy": round(correct / total, 2) if total > 0 else 0.0,
    }
    
def get_language_usage_stats(db: Session) -> Dict[str, int]:
    usage = defaultdict(int)
    
    for dialogue in db.query(DialogueLog).all():
        usage[dialogue.language] += 1
        
    for mentor in db.query(MentorInteraction).all():
        usage[mentor.language] += 1
        
    return dict(usage)

def average_xp_per_user(db: Session) -> float:
    # sourcery skip: assign-if-exp, reintroduce-else
    total_users = count_total_users(db)
    if total_users == 0:
        return 0.0
    return round(total_xp_earned(db) / total_users, 2)

def get_all_metrics(db: Session) -> Dict[str, Any]:
    return {
        "total_users": count_total_users(db),
        "total_xp": total_xp_earned(db),
        "avg_xp_per_user": average_xp_per_user(db),
        "language_usage": get_language_usage_stats(db)
    }
