# === Stage 32: Add pagination helpers for long console output ===
# Project: StudyHub
def paginate_output(text, max_lines=15):
    """Yields chunks of text with line numbers for long console output."""
    lines = text.splitlines()
    total_lines = len(lines)
    chunk_size = (total_lines + max_lines - 1) // max_lines if max_lines > 0 else 1
    
    for i in range(0, total_lines, chunk_size):
        chunk = lines[i:i+chunk_size]
        print(f"--- Chunk {i//chunk_size + 1}/{total_lines} ---")
        for j, line in enumerate(chunk, start=i+1):
            if len(line) > 80:
                print(f"{j:>4}: {line[:77]}...")
            else:
                print(f"{j:>4}: {line}")

def format_progress_summary(data, max_entries=5):
    """Formats a list of progress entries into a paginated summary."""
    output = []
    if not data:
        return "No progress recorded."
    
    for i in range(min(len(data), max_entries)):
        entry = data[i]
        status_icon = "[✓]" if entry.get("completed") else "[ ]"
        line = f"{status_icon} {entry['subject']}: {entry['progress']}%"
        
        # Truncate long descriptions for readability
        desc = entry.get('description', '')
        if len(line) + len(desc) > 100 and desc:
            line += " ... (see details below)"
        output.append(line)
    
    return "\n".join(output)

if __name__ == "__main__":
    # Example usage with dummy data
    sample_data = [
        {"subject": "Python Basics", "progress": 100, "completed": True},
        {"subject": "Data Structures", "progress": 85, "completed": False},
        {"subject": "Algorithms", "progress": 45, "completed": False},
        {"subject": "Web Development", "progress": 30, "completed": False},
        {"subject": "Database Design", "progress": 60, "completed": True},
    ]
    
    print("StudyHub Progress Summary:")
    summary = format_progress_summary(sample_data)
    print(summary)
