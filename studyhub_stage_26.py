# === Stage 26: Add weekly summary calculations ===
# Project: StudyHub
def calculate_weekly_summary(lessons, cards, checkpoints):
    from datetime import datetime, timedelta
    today = datetime.now().date()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    week_end = (week_start + timedelta(days=6)).isoformat()

    weekly_lessons = [l for l in lessons if week_start <= l['completed_at'] <= week_end]
    weekly_cards = [c for c in cards if week_start <= c['reviewed_at'] <= week_end]
    weekly_checkpoints = [cp for cp in checkpoints if week_start <= cp['passed_at'] <= week_end]

    total_lessons_completed = len(weekly_lessons)
    total_cards_reviewed = len(weekly_cards)
    total_checkpoints_passed = len(weekly_checkpoints)

    summary = {
        "week_start": week_start,
        "week_end": week_end,
        "lessons_completed": total_lessons_completed,
        "cards_reviewed": total_cards_reviewed,
        "checkpoints_passed": total_checkpoints_passed,
        "total_activities": total_lessons_completed + total_cards_reviewed + total_checkpoints_passed
    }

    return summary
