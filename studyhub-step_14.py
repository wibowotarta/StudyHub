# === Stage 14: Add file load support with fallback demo data ===
# Project: StudyHub
def load_study_data(path=None):
    if path and os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            "lessons": [{"id": 1, "title": "Intro", "content": "Welcome to StudyHub."}],
            "cards": [{"front": "What is Python?", "back": "A high-level programming language."}],
            "checkpoints": [],
            "progress_summary": {"completed_lessons": 0, "total_cards_reviewed": 0}
        }
