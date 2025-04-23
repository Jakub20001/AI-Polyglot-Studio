from sqlalchemy.orm import Session
from collections import defaultdict
from typing import Dict, Any
from backend import models

def count_total_users(db: Session) -> int:
    return db.query(models.User).count()

def total_xp_earned(db: Session) -> int:
    return sum([xp.points for xp in db.query(models.XP).all()])

def get_user_quiz_stats(db: Session, user_id: int) -> Dict[str, Any]:
    attempts = db.query(models.QuizAnswer).filter(models.QuizAnswer.user_id == user_id).all()
    total = len(attempts)
    correct = sum([1 for a in attempts if a.is_correct])
    return {
        "total_attempts": total,
        "correct_answers": correct,
        "accuracy": round(correct / total, 2) if total > 0 else 0
    }
    
def get_language_usage_stats(db: Session) -> Dict[str, int]:
    usage = defaultdict(int)
    for dialogue in db.query(models.DialogueLog).all():
        usage[dialogue.language] += 1
    for mentor in db.query(models.MentorInteraction).all():
        usage[mentor.language] += 1
    return dict(usage)

def average_xp_per_user(db: Session) -> float:
    users = count_total_users(db)
    if users == 0:
        return 0
    return round(total_xp_earned(db) / users, 2)

def get_all_metrics(db: Session) -> Dict[str, Any]:
    return {
        "total_users": count_total_users(db),
        "total_xp": total_xp_earned(db),
        "avg_xp_per_user": average_xp_per_user(db),
        "language_usage": get_language_usage_stats(db)
    }