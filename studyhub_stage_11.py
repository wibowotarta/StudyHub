# === Stage 11: Add JSON export for the current application state ===
# Project: StudyHub
def export_state(data):
    import json
    with open("studyhub_state.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"State exported to studyhub_state.json ({len(json.dumps(data))} bytes)")

if __name__ == "__main__":
    # Example usage with a mock state object
    sample_state = {
        "lessons": [{"id": 1, "title": "Python Basics", "completed": True}],
        "cards": [{"front": "What is Python?", "back": "A high-level programming language."}],
        "checkpoints": [{"date": "2023-10-01", "status": "passed"}],
        "summary": {"total_lessons": 5, "completed_lessons": 3}
    }
    export_state(sample_state)
