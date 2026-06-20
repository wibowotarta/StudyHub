# === Stage 35: Add active user switching and user-specific records ===
# Project: StudyHub
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import uuid
from datetime import datetime

@dataclass
class User:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = "Unknown"
    active_lesson_id: Optional[str] = None
    
    def activate(self, lesson_id: str) -> None:
        self.active_lesson_id = lesson_id

@dataclass
class UserRecord:
    user: User
    timestamp: datetime = field(default_factory=datetime.now)
    status: str = "pending"
    
    @property
    def summary(self) -> str:
        return f"{self.user.name} ({self.timestamp.strftime('%H:%M')}) - {self.status}"

class StudyHubManager:
    _users: Dict[str, User] = {}
    _records: List[UserRecord] = []
    
    @classmethod
    def register_user(cls, name: str) -> User:
        if name not in cls._users:
            cls._users[name] = User(name=name)
        return cls._users[name]
    
    @classmethod
    def switch_active_user(cls, user_name: str, lesson_id: Optional[str] = None) -> Optional[User]:
        user = cls._users.get(user_name)
        if not user:
            raise ValueError(f"User {user_name} not found")
        if lesson_id:
            user.activate(lesson_id)
        return user
    
    @classmethod
    def log_checkpoint(cls, status: str) -> UserRecord:
        active = cls._users.get("current_user") or list(cls._users.values())[0]
        record = UserRecord(user=active, status=status)
        cls._records.append(record)
        return record
    
    @classmethod
    def get_progress_summary(cls) -> List[str]:
        return [r.summary for r in sorted(cls._records, key=lambda x: x.timestamp)]
