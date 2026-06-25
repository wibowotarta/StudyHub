# === Stage 53: Add command help text and usage examples ===
# Project: StudyHub
def print_help():
    """Display usage instructions and examples for StudyHub."""
    help_text = (
        "StudyHub - Shared Study Planner\n"
        "Usage: python studyhub.py <command>\n"
        "\n"
        "Commands:\n"
        "  add-lesson      Add a new lesson with title, duration and topic.\n"
        "  create-card     Create flashcards for a specific lesson.\n"
        "  set-checkpoint  Define a progress checkpoint (e.g., after chapter X).\n"
        "  show-progress   Display current completion summary.\n"
        "\n"
        "Examples:\n"
        "  python studyhub.py add-lesson --title 'Intro to Python' --duration 45\n"
        "  python studyhub.py create-card --lesson 'Intro to Python' --term 'print()' --answer 'Output text'\n"
        "  python studyhub.py set-checkpoint --lesson 'Data Structures' --progress 0.75\n"
        "  python studyhub.py show-progress\n"
    )
    print(help_text)
