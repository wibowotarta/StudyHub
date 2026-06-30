# === Stage 72: Add Markdown report export ===
# Project: StudyHub
def export_progress_to_markdown(lessons, cards, checkpoints):
    """Generate a compact markdown report from study data."""
    lines = ["# StudyHub Progress Report", ""]
    
    if lessons:
        lines.append("## Lessons Completed")
        for lesson in sorted(lessons, key=lambda x: x.get('date', '')):
            title = lesson.get('title', 'Untitled')
            date = lesson.get('date', '')
            lines.append(f"- {title} ({date})")
        lines.append("")

    if cards:
        lines.append("## Flashcards Reviewed")
        for card in sorted(cards, key=lambda x: x.get('reviewed_at', '')):
            front = card.get('front', 'N/A')[:30] + "..." if len(card.get('front', '')) > 30 else card.get('front', '')
            lines.append(f"- {front}")
        lines.append("")

    if checkpoints:
        lines.append("## Checkpoints Reached")
        for cp in sorted(checkpoints, key=lambda x: x.get('date', '')):
            name = cp.get('name', 'N/A')
            date = cp.get('date', '')
            status = "✅" if cp.get('completed') else "⏳"
            lines.append(f"- {status} {name} ({date})")
        lines.append("")

    return "\n".join(lines)
