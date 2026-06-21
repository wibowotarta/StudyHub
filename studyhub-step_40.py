# === Stage 40: Add plain text report export ===
# Project: StudyHub
def export_report(lessons, cards, checkpoints):
    with open("studyhub_report.txt", "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("STUDYHUB PROGRESS REPORT\n")
        f.write("=" * 40 + "\n\n")
        
        if lessons:
            f.write("LESSONS COMPLETED:\n")
            for i, lesson in enumerate(lessons, 1):
                f.write(f"  {i}. {lesson['title']} ({lesson.get('status', 'new')})\n")
            f.write("\n")

        if cards:
            f.write("FLASHCARDS SUMMARY:\n")
            for i, card in enumerate(cards, 1):
                term = card.get('term', '')[:30] + "..." if len(card.get('term', '')) > 30 else card.get('term', '')
                def_term = card.get('definition', '')[:40] + "..." if len(card.get('definition', '')) > 40 else card.get('definition', '')
                f.write(f"  {i}. Q: {term} -> A: {def_term}\n")
            f.write("\n")

        if checkpoints:
            f.write("CHECKPOINTS STATUS:\n")
            for i, cp in enumerate(checkpoints, 1):
                status = "DONE" if cp.get('completed', False) else "PENDING"
                f.write(f"  {i}. [{status}] {cp['name']}\n")

        total_lessons = len(lessons)
        completed_lessons = sum(1 for l in lessons if l.get('status') == 'done')
        
        f.write("-" * 40 + "\n")
        f.write(f"TOTAL LESSONS: {total_lessons}\n")
        f.write(f"COMPLETED: {completed_lessons}\n")
        progress = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
        f.write(f"PROGRESS: {progress:.1f}%\n")
        f.write("=" * 40 + "\n")
