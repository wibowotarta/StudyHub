# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: StudyHub
def format_progress_summary(lessons: list, cards: dict) -> str:
    """Generate a human-readable progress summary from study data."""
    lines = ["=== StudyHub Progress Report ===", f"Total Lessons Completed: {len([l for l in lessons if l.get('done')])}/{len(lessons)}"]
    total_cards = sum(len(c.get('items', [])) for c in cards.values())
    mastered_cards = sum(sum(1 for i in c.get('items', []) if i.get('mastered')) for c in cards.values())
    lines.append(f"Total Flashcards: {total_cards}")
    lines.append(f"Mastered Cards: {mastered_cards} ({int(mastered_cards/total_cards*100) if total_cards else 0}%)")
    last_checkpoint = max((l.get('checkpoint', 'N/A') for l in lessons), default='N/A')
    lines.append(f"Latest Checkpoint: {last_checkpoint}")
    return "\n".join(lines)
