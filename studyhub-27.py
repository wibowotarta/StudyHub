# === Stage 27: Add monthly summary calculations ===
# Project: StudyHub
def calculate_monthly_summary(lessons, cards, checkpoints):
    from datetime import date
    current_month = date.today().strftime("%Y-%m")
    monthly_lessons = [l for l in lessons if l.get('start_date', '').startswith(current_month)]
    monthly_cards = [c for c in cards if c.get('created_at', '').startswith(current_month)]
    monthly_checkpoints = [cp for cp in checkpoints if cp.get('date', '').startswith(current_month)]
    total_lessons_completed = len([l for l in monthly_lessons if l.get('status') == 'completed'])
    total_cards_created = len(monthly_cards)
    total_checkpoints_passed = len([cp for cp in monthly_checkpoints if cp.get('passed')])
    progress_percentage = round((total_lessons_completed / max(len(monthly_lessons), 1)) * 100, 2)
    summary = {
        "month": current_month,
        "lessons_completed": total_lessons_completed,
        "cards_created": total_cards_created,
        "checkpoints_passed": total_checkpoints_passed,
        "progress_percentage": progress_percentage
    }
    return summary
