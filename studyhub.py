# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: StudyHub
from typing import List, Dict, Any
from dataclasses import dataclass, field
import uuid

@dataclass
class Lesson:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    title: str = ""
    content: str = ""
    difficulty: int = 1

@dataclass
class Flashcard:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    question: str = ""
    answer: str = ""

@dataclass
class Checkpoint:
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    lesson_id: str = ""
    passed: bool = False
    timestamp: float = field(default_factory=float)

class StudyHubState:
    def __init__(self):
        self.lessons: Dict[str, Lesson] = {}
        self.cards: Dict[str, Flashcard] = {}
        self.checkpoints: Dict[str, Checkpoint] = {}
    
    def add_lesson(self, title: str, content: str, difficulty: int = 1) -> Lesson:
        lesson = Lesson(title=title, content=content, difficulty=difficulty)
        self.lessons[lesson.id] = lesson
        return lesson
    
    def add_card(self, question: str, answer: str) -> Flashcard:
        card = Flashcard(question=question, answer=answer)
        self.cards[card.id] = card
        return card
    
    def create_checkpoint(self, lesson_id: str, passed: bool = True) -> Checkpoint:
        cp = Checkpoint(lesson_id=lesson_id, passed=passed)
        self.checkpoints[cp.id] = cp
        return cp
    
    def get_progress_summary(self) -> Dict[str, Any]:
        total_lessons = len(self.lessons)
        completed_lessons = sum(1 for cp in self.checkpoints.values() if cp.passed)
        total_cards = len(self.cards)
        return {
            "total_lessons": total_lessons,
            "completed_lessons": completed_lessons,
            "completion_rate": (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0,
            "total_cards": total_cards
        }

# Demo dataset initialization
demo_state = StudyHubState()
demo_state.add_lesson("Introduction to Python", "Variables, loops, and functions basics.", difficulty=1)
demo_state.add_card("What is a variable?", "A named storage location in memory.")
demo_state.add_card("What does print() do?", "Displays output to the console.")
print(demo_state.get_progress_summary())
