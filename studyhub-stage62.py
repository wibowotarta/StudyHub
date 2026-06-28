# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: StudyHub
def calculate_priority(lesson: dict) -> int:
    """Calculate priority score based on deadline urgency and completion status."""
    days_left = (lesson['due_date'] - lesson['created_at']).days if 'due_date' in lesson else 30
    is_completed = lesson.get('completed', False)
    importance = lesson.get('importance', 1)
    return int((7 - min(days_left, 7)) * importance + (1 if not is_completed else 0))
