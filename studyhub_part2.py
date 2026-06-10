# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: StudyHub
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List
from enum import Enum

class LessonStatus(Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    SKIPPED = "skipped"

@dataclass
class StudyCard:
    front: str
    back: str
    category: str

@dataclass
class Lesson:
    title: str
    content: str
    status: LessonStatus = LessonStatus.PLANNED
    estimated_minutes: int = 0
    created_by: Optional[str] = None
    added_at: date = field(default_factory=date.today)

@dataclass
class Checkpoint:
    lesson_id: str
    passed: bool
    notes: str = ""
    completed_at: Optional[date] = None

@dataclass
class ProgressSummary:
    total_lessons: int = 0
    completed_lessons: int = 0
    cards_reviewed: int = 0
    last_updated: date = field(default_factory=date.today)
