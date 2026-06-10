# === Stage 4: Implement create operations for the primary records ===
# Project: StudyHub
from datetime import datetime

def create_lesson(title, description, duration_minutes):
    lesson_id = f"LESSON_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    return {
        "id": lesson_id,
        "title": title,
        "description": description,
        "duration_minutes": duration_minutes,
        "created_at": datetime.now().isoformat(),
        "status": "active"
    }

def create_card(front_text, back_text):
    card_id = f"CARD_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    return {
        "id": card_id,
        "front": front_text,
        "back": back_text,
        "created_at": datetime.now().isoformat()
    }

def create_checkpoint(lesson_id, question, correct_answer):
    checkpoint_id = f"CHECKPOINT_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    return {
        "id": checkpoint_id,
        "lesson_id": lesson_id,
        "question": question,
        "correct_answer": correct_answer,
        "created_at": datetime.now().isoformat()
    }

def create_progress_summary(user_id, lesson_id):
    summary_id = f"SUMMARY_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    return {
        "id": summary_id,
        "user_id": user_id,
        "lesson_id": lesson_id,
        "completed_at": datetime.now().isoformat(),
        "score": 100
    }
