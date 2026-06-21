# === Stage 41: Add plain text import for a simple line-based format ===
# Project: StudyHub
import csv
from typing import List, Dict, Any

def load_plain_text_lessons(filepath: str) -> List[Dict[str, Any]]:
    """Load lessons from a simple line-based text file where each line is 'id|title|content'."""
    lessons = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('|')
            if len(parts) >= 3:
                lesson_id = int(parts[0])
                title = parts[1]
                content = parts[2]
                lessons.append({'id': lesson_id, 'title': title, 'content': content})
    return sorted(lessons, key=lambda x: x['id'])

def save_progress_summary(filepath: str, progress_data: Dict[int, int]) -> None:
    """Save a simple summary of completed checkpoints to a text file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for lesson_id in sorted(progress_data.keys()):
            status = "completed" if progress_data[lesson_id] > 0 else "pending"
            f.write(f"{lesson_id}|{status}\n")
