# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: StudyHub
SETTINGS = {
    "theme": "dark",
    "notifications": True,
    "sound_effects": False,
}

def update_settings(key: str, value):
    if key in SETTINGS and isinstance(SETTINGS[key], type(value)):
        SETTINGS[key] = value
        return True
    raise ValueError(f"Invalid setting or type mismatch for '{key}'")
