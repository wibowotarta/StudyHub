# === Stage 55: Add a setting to disable colorized output ===
# Project: StudyHub
class ColorSettings:
    def __init__(self, enable_color=True):
        self.enable_color = enable_color
    
    @staticmethod
    def is_enabled():
        return os.environ.get("STUDYHUB_COLOR", "true").lower() != "false" and not hasattr(ColorSettings, "_disabled")

def disable_colors():
    ColorSettings._disabled = True
