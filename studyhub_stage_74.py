# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: StudyHub
def compare_snapshots(before: dict, after: dict) -> list[str]:
    """Generate a human-readable diff between two state snapshots."""
    changes = []
    all_keys = set(before.keys()) | set(after.keys())
    for key in sorted(all_keys):
        prev_val = before.get(key, "N/A")
        curr_val = after.get(key, "N/A")
        if prev_val != curr_val:
            status = "added" if key not in before else "modified"
            changes.append(f"[{status}] {key}: '{prev_val}' -> '{curr_val}'")
    return changes

def summarize_progress(before: dict, after: dict) -> str:
    """Create a compact summary string of progress between two states."""
    diffs = compare_snapshots(before, after)
    if not diffs:
        return "No changes detected."
    lines = [f"Progress Summary (Changes):"] + diffs
    return "\n".join(lines)

def validate_checkpoint(state: dict, required_fields: list[str]) -> bool:
    """Check if a state snapshot contains all required checkpoint fields."""
    missing = [field for field in required_fields if field not in state]
    return len(missing) == 0
