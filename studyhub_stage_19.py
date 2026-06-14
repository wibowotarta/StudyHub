# === Stage 19: Add undo support for the last simple mutation ===
# Project: StudyHub
class UndoManager:
    def __init__(self, max_history=10):
        self.history = []
        self.max_size = max_history

    def record(self, action_type, data):
        if len(self.history) >= self.max_size:
            del self.history[0]
        self.history.append({"type": action_type, "data": data})

    def undo_last(self):
        if not self.history:
            return None
        last = self.history.pop()
        return {"action": last["type"], "payload": last["data"]}
