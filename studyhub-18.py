# === Stage 18: Add an activity log with timestamps and action names ===
# Project: StudyHub
import time
from datetime import datetime, timezone
from typing import Optional

class ActivityLogger:
    def __init__(self):
        self._log = []

    def log(self, action_name: str, details: Optional[str] = None) -> None:
        timestamp = datetime.now(timezone.utc).isoformat()
        entry = {"timestamp": timestamp, "action": action_name, "details": details}
        self._log.append(entry)
        print(f"[{timestamp}] {action_name}: {details or ''}")

    def get_summary(self) -> list:
        return sorted(self._log, key=lambda x: x["timestamp"])
