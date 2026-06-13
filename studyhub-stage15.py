# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: StudyHub
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        clean_text = text.strip().lower()
        if clean_text in self.handlers:
            return self.handlers[clean_text]()
        return None
