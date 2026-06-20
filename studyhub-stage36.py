# === Stage 36: Add templates for quickly creating common records ===
# Project: StudyHub
class RecordTemplates:
    def __init__(self):
        self.templates = {
            "lesson": lambda title, duration_min=30: {"type": "lesson", "title": title, "duration_minutes": duration_min},
            "flashcard_front": lambda q: {"type": "card", "front": q, "back": None},
            "flashcard_back": lambda a: {"type": "card", "front": None, "back": a},
            "checkpoint": lambda topic, passed=True: {"type": "checkpoint", "topic": topic, "passed": passed},
        }

    def create(self, name, **kwargs):
        if name in self.templates:
            return self.templates[name](**kwargs)
        raise ValueError(f"Unknown template: {name}")
