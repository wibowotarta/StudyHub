# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: StudyHub
def validate_study_plan(plan):
    warnings = []
    errors = []
    for lesson in plan.get("lessons", []):
        if not lesson.get("title"):
            errors.append(f"Lesson missing title: {lesson}")
        elif len(lesson["content"]) > 5000:
            warnings.append(f"Lesson content too long: {lesson['title']}")
    for card in plan.get("cards", []):
        if not card.get("front"):
            errors.append(f"Flashcard missing front text: {card}")
        elif not card.get("back"):
            errors.append(f"Flashcard missing back text: {card}")
    for checkpoint in plan.get("checkpoints", []):
        if not isinstance(checkpoint["date"], str) or len(checkpoint["date"]) < 10:
            warnings.append(f"Invalid date format for checkpoint: {checkpoint['title']}")
    return {"warnings": warnings, "errors": errors}
