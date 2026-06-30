# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: StudyHub
def clear_state():
    if input("Are you sure you want to reset all progress? (y/n) ") != "y":
        return
    lessons = {}
    cards = []
    checkpoints = set()
    summaries = {}
    save_data(lessons, cards, checkpoints, summaries)
