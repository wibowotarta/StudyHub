# === Stage 37: Add recommendations for the next useful action ===
# Project: StudyHub
from typing import List, Dict, Any
import random

def generate_next_action(lessons: List[Dict[str, Any]], cards: int, checkpoints_passed: int) -> str:
    if lessons and random.random() < 0.6:
        topic = random.choice(lessons).get('topic', 'General Study')
        return f"Review {topic} notes for 15 minutes."
    elif cards > 0 and random.random() < 0.3:
        return "Flashcard session: 20 new terms."
    elif checkpoints_passed < len(checkpoints_passed):
        return "Complete next checkpoint task."
    else:
        return "Take a 10-minute break or review progress summary."
