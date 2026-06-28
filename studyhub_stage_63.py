# === Stage 63: Add relationships between records where useful ===
# Project: StudyHub
from typing import Optional, List, Dict
import uuid

class StudyRecord:
    def __init__(self, id: str = None, title: str = "", content: str = ""):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.content = content
        self.related_lessons: List[str] = []  # Links to Lesson records
        self.checkpoints: List[Dict] = []    # Linked checkpoint data

class Lesson(StudyRecord):
    def __init__(self, id: str = None, topic: str = "", difficulty: int = 1):
        super().__init__()
        self.id = id or str(uuid.uuid4())
        self.topic = topic
        self.difficulty = difficulty
        self.cards: List[str] = []           # Links to Card records

class Card(StudyRecord):
    def __init__(self, id: str = None, front: str = "", back: str = ""):
        super().__init__()
        self.id = id or str(uuid.uuid4())
        self.front = front
        self.back = back
        self.lesson_id: Optional[str] = None # Back-reference to Lesson

class Checkpoint(StudyRecord):
    def __init__(self, id: str = None, status: str = "pending", score: float = 0.0):
        super().__init__()
        self.id = id or str(uuid.uuid4())
        self.status = status
        self.score = score
        self.lesson_id: Optional[str] = None # Back-reference to Lesson
