# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: StudyHub
def update_lesson_progress(lesson_id, new_status):
    """Update a lesson's status, handling missing records gracefully."""
    try:
        with open("studyhub_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return False, "Data file not found"

    if lesson_id not in data.get("lessons", {}):
        return False, f"Lesson {lesson_id} not found"

    data["lessons"][lesson_id]["status"] = new_status
    data["lessons"][lesson_id]["updated_at"] = datetime.now().isoformat()

    try:
        with open("studyhub_data.json", "w") as f:
            json.dump(data, f, indent=2)
        return True, "Lesson updated successfully"
    except Exception as e:
        return False, f"Failed to save changes: {str(e)}"

def add_checkpoint(lesson_id, checkpoint_text):
    """Add a new checkpoint to an existing lesson."""
    try:
        with open("studyhub_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return False, "Data file not found"

    if lesson_id not in data.get("lessons", {}):
        return False, f"Lesson {lesson_id} not found"

    checkpoint_id = len(data["lessons"][lesson_id]["checkpoints"]) + 1
    data["lessons"][lesson_id]["checkpoints"].append({
        "id": checkpoint_id,
        "text": checkpoint_text,
        "completed": False,
        "created_at": datetime.now().isoformat()
    })

    try:
        with open("studyhub_data.json", "w") as f:
            json.dump(data, f, indent=2)
        return True, f"Checkpoint {checkpoint_id} added to lesson {lesson_id}"
    except Exception as e:
        return False, f"Failed to save changes: {str(e)}"

def mark_checkpoint_complete(lesson_id, checkpoint_id):
    """Mark a specific checkpoint as completed."""
    try:
        with open("studyhub_data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        return False, "Data file not found"

    if lesson_id not in data.get("lessons", {}):
        return False, f"Lesson {lesson_id} not found"

    checkpoints = data["lessons"][lesson_id].get("checkpoints", [])
    if not checkpoints:
        return False, "No checkpoints exist for this lesson"

    try:
        checkpoint_index = next((i for i, c in enumerate(checkpoints) if c["id"] == checkpoint_id), None)
        if checkpoint_index is None:
            return False, f"Checkpoint {checkpoint_id} not found in lesson {lesson_id}"
        
        checkpoints[checkpoint_index]["completed"] = True
        checkpoints[checkpoint_index]["completed_at"] = datetime.now().isoformat()

        with open("studyhub_data.json", "w") as f:
            json.dump(data, f, indent=2)
        return True, f"Checkpoint {checkpoint_id} marked complete"
    except Exception as e:
        return False, f"Failed to save changes: {str(e)}"
