# === Stage 25: Add daily summary calculations ===
# Project: StudyHub
def calculate_daily_summary(lessons, cards, checkpoints):
    total_lessons = len([l for l in lessons if l.get('completed', False)])
    total_cards = len([c for c in cards if c.get('mastered', False)])
    total_checkpoints = len([cp for cp in checkpoints if cp.get('passed', False)])
    
    progress_rate = 0.0
    if (total_lessons + total_cards + total_checkpoints) > 0:
        progress_rate = ((total_lessons * 10) + (total_cards * 5) + (total_checkpoints * 2)) / \
                        (len(lessons) * 10 + len(cards) * 5 + len(checkpoints) * 2)
    
    summary_text = f"Daily Progress: {progress_rate:.1%} | Lessons: {total_lessons}/{len(lessons)} | " \
                   f"Cards: {total_cards}/{len(cards)} | Checkpoints: {total_checkpoints}/{len(checkpoints)}"
    return summary_text
