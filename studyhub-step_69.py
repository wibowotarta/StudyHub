# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: StudyHub
def reset_demo_data():
    from datetime import date, timedelta
    if __name__ == "__main__":
        print("Resetting demo data...")
        # Clear existing progress for all users to start fresh
        with open("progress.json", "w") as f:
            f.write("{}\n")
        # Re-populate core lessons and cards
        with open("lessons.json", "w") as f:
            import json
            data = {
                "math": [{"id": 1, "title": "Algebra Basics", "content": "x + y = z"}],
                "history": [{"id": 2, "title": "WWII Overview", "content": "1939-1945 conflict"}]
            }
            json.dump(data, f)
        # Re-populate study cards
        with open("cards.json", "w") as f:
            import json
            data = [
                {"front": "What is the capital of France?", "back": "Paris"},
                {"front": "Solve for x: 2x + 4 = 10", "back": "3"}
            ]
            json.dump(data, f)
        # Re-populate checkpoints with today's date
        with open("checkpoints.json", "w") as f:
            import json
            today = (date.today() - timedelta(days=2)).isoformat()
            tomorrow = (date.today()).isoformat()
            data = [
                {"id": 1, "title": "Math Quiz", "due_date": today},
                {"id": 2, "title": "History Essay", "due_date": tomorrow}
            ]
            json.dump(data, f)
        # Re-populate progress summaries
        with open("summaries.json", "w") as f:
            import json
            data = {
                "user_1": {"completed": 0, "pending": 2},
                "user_2": {"completed": 0, "pending": 2}
            }
            json.dump(data, f)
        print("Demo data reset complete.")
