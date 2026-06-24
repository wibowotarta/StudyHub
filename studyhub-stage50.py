# === Stage 50: Add unit tests for import and export behavior ===
# Project: StudyHub
import json, os
from pathlib import Path
def test_import_export():
    data = {"lessons": [{"id": 1, "title": "Math"}], "cards": [], "checkpoints": []}
    temp_dir = Path("temp_test")
    temp_dir.mkdir(exist_ok=True)
    file_path = temp_dir / "studyhub.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    assert os.path.exists(file_path), "Exported file not created"
    loaded_data = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
    except FileNotFoundError:
        raise AssertionError("Import failed: File not found")
    assert loaded_data["lessons"][0]["title"] == "Math", "Data mismatch after import"
    temp_dir.rmdir()
