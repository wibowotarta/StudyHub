# === Stage 13: Add file save support using a configurable path ===
# Project: StudyHub
import os, json, sys
from pathlib import Path

def get_data_path():
    base = Path.home() / ".studyhub"
    app_dir = base / "data"
    if not app_dir.exists():
        app_dir.mkdir(parents=True)
    return str(app_dir)

def save_state(state: dict, path: str | None = None):
    if path is None:
        p = Path(get_data_path()) / "state.json"
    else:
        p = Path(path)
    try:
        with open(p, 'w', encoding='utf-8') as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving state to {p}: {e}")
        return False

def load_state(path: str | None = None) -> dict:
    if path is None:
        p = Path(get_data_path()) / "state.json"
    else:
        p = Path(path)
    try:
        with open(p, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"No state file found at {p}")
        return {}
    except Exception as e:
        print(f"Error loading state from {p}: {e}")
        return {}

if __name__ == "__main__":
    # Example usage for CLI or script entry point
    if len(sys.argv) > 1 and sys.argv[1] in ["save", "load"]:
        cmd = sys.argv[1]
        path = sys.argv[2] if len(sys.argv) > 2 else None
        data = {"lessons": [], "cards": []} if cmd == "load" else {}
        if cmd == "save":
            save_state(data, path)
        elif cmd == "load":
            print(json.dumps(load_state(path), indent=2))
