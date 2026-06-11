# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: StudyHub
def format_lesson(lesson):
    return f"[{lesson['id']}] {lesson['title']} ({len(lesson['content'])} chars)"

def format_card(card):
    return f"Card: {card['question']} -> {card['answer']}"

def format_checkpoint(checkpoint):
    status = "✓" if checkpoint['completed'] else "○"
    return f"{status} {checkpoint['name']}: {checkpoint['description'][:30]}..."

def render_summary(progress, lessons, cards, checkpoints):
    lines = [f"=== StudyHub Progress ===", f"Lessons: {len(lessons)} | Cards: {len(cards)}"]
    for c in checkpoints:
        lines.append(format_checkpoint(c))
    return "\n".join(lines)
