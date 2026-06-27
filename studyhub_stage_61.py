# === Stage 61: Add performance timing for core list and search operations ===
# Project: StudyHub
import time
from functools import wraps

def timed_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration_ms = (end - start) * 1000
        print(f"[TIMED] {func.__name__} took {duration_ms:.2f}ms")
        return result
    return wrapper

class StudyHubTimed:
    def __init__(self, data):
        self.data = data
    
    @timed_operation
    def search_lessons(self, query):
        return [lesson for lesson in self.data if query.lower() in lesson.title.lower()]
    
    @timed_operation
    def get_progress_summary(self):
        completed = sum(1 for item in self.data if item.get('completed', False))
        total = len(self.data)
        return {'total': total, 'completed': completed, 'percentage': (completed / total * 100) if total else 0}

# Usage example:
# hub = StudyHubTimed(lessons_list)
# results = hub.search_lessons("python")
# summary = hub.get_progress_summary()
