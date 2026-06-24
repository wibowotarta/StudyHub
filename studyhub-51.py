# === Stage 51: Add unit tests for search and filter behavior ===
# Project: StudyHub
def test_search_and_filter():
    from study_hub import StudyHub
    hub = StudyHub()
    # Add sample data
    hub.add_lesson("Math", "Algebra", 10)
    hub.add_card("Math", "x^2 + y^2 = r^2")
    hub.add_checkpoint("Math", "Quiz 1", True)
    
    # Test search by keyword in lesson title
    results = hub.search_lessons("Algebra")
    assert len(results) == 1 and results[0].title == "Algebra"
    
    # Test filter by subject
    filtered = hub.filter_by_subject("Math")
    subjects_count = sum(1 for _ in filtered if _.subject == "Math")
    assert subjects_count >= 3
    
    # Test combined search and filter (empty result)
    results_empty = hub.search_lessons("Physics")
    assert len(results_empty) == 0
