# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: StudyHub
def seed_demo_data(db):
    from datetime import timedelta, date
    lessons = [
        {"title": "Python Basics", "content": "Variables, loops, functions.", "duration_minutes": 45},
        {"title": "Data Structures", "content": "Lists, dicts, sets comprehensions.", "duration_minutes": 60},
        {"title": "Async IO", "content": "async/await patterns and concurrency.", "duration_minutes": 90}
    ]
    cards = [
        {"front": "What is a list?", "back": "Ordered, mutable collection of items."},
        {"front": "How to run async code?", "back": "Use asyncio.run() or event loop."}
    ]
    checkpoints = []
    for i in range(3):
        checkpoints.append({
            "lesson_id": i + 1,
            "title": f"Checkpoint {i+1}",
            "date": date.today() - timedelta(days=i*2),
            "status": "completed" if i < 2 else "pending"
        })
    summaries = [
        {"user_id": "u1", "total_lessons": len(lessons), "cards_reviewed": len(cards)},
        {"user_id": "u2", "total_lessons": len(lessons), "cards_reviewed": 0}
    ]
    db["lessons"].extend(lessons)
    db["flashcards"].extend(cards)
    db["checkpoints"].extend(checkpoints)
    db["summaries"].extend(summaries)
