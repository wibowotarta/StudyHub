# === Stage 67: Add a function that returns key project metrics ===
# Project: StudyHub
def get_project_metrics(lessons, cards, checkpoints):
    total_lessons = len(lessons)
    completed_lessons = sum(1 for l in lessons if l.get('status') == 'completed')
    completion_rate = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0

    total_cards = len(cards)
    mastered_cards = sum(1 for c in cards if c.get('mastery_level', 0) >= 4)
    mastery_rate = (mastered_cards / total_cards * 100) if total_cards > 0 else 0

    active_checkpoints = sum(1 for cp in checkpoints if not cp.get('completed'))
    completed_checkpoints = len(checkpoints) - active_checkpoints
    checkpoint_progress = (completed_checkpoints / len(checkpoints) * 100) if checkpoints else 0

    return {
        'total_lessons': total_lessons,
        'completed_lessons': completed_lessons,
        'lesson_completion_rate': round(completion_rate, 2),
        'total_cards': total_cards,
        'mastered_cards': mastered_cards,
        'card_mastery_rate': round(mastery_rate, 2),
        'active_checkpoints': active_checkpoints,
        'completed_checkpoints': completed_checkpoints,
        'checkpoint_progress': round(checkpoint_progress, 2)
    }
