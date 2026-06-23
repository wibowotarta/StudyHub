# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: StudyHub
def run_demo():
    from datetime import date, timedelta
    today = date.today()
    
    # Create a sample lesson for "Python Basics"
    lesson_id = 101
    title = "Introduction to Variables"
    content = """Variables are containers for storing data values. 
In Python, variables do not need explicit declaration."""
    checkpoint_date = today + timedelta(days=3)
    
    # Create a flashcard associated with the lesson
    card_id = 501
    front = "What is a variable?"
    back = "A named storage location for data."
    
    # Simulate progress summary generation
    completed_lessons = [lesson_id]
    pending_checkpoints = [checkpoint_date.strftime("%Y-%m-%d")]
    
    print(f"=== StudyHub Demo Scenario ===")
    print(f"Lesson {lesson_id}: '{title}' created.")
    print(f"Content preview: {content[:30]}...")
    print(f"Flashcard {card_id} added:")
    print(f"  Front: {front}")
    print(f"  Back: {back}")
    print(f"Checkpoint scheduled for: {' '.join(pending_checkpoints)}")
    print(f"Progress summary generated with {len(completed_lessons)} completed items.")
