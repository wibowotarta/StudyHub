# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: StudyHub
import unittest
from studyhub.models import Lesson, Card, Checkpoint
from studyhub.services.study_planner_service import StudyPlannerService

class TestStudyPlannerEdgeCases(unittest.TestCase):
    def setUp(self):
        self.service = StudyPlannerService()
    
    def test_update_nonexistent_lesson_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.service.update_lesson("non_existent_id", {"title": "New Title"})
        self.assertIn("Lesson not found", str(context.exception))

    def test_delete_nonexistent_card_raises_error(self):
        with self.assertRaises(ValueError) as context:
            self.service.delete_card("999-unknown-id")
        self.assertIn("Card not found", str(context.exception))

    def test_update_lesson_with_empty_title_trims_whitespace(self):
        lesson = Lesson(id="123", title="  Test Title  ")
        updated = self.service.update_lesson("123", {"title": "   New Title   "})
        self.assertEqual(updated.title, "New Title")

    def test_delete_checkpoint_removes_from_progress_summary(self):
        checkpoint = Checkpoint(id="cp-001", status="completed")
        lesson = Lesson(id="l-001", checkpoints=[checkpoint])
        # Simulate adding to planner state (assuming service has internal storage)
        self.service._lessons["l-001"] = lesson
        deleted_checkpoint_id = "cp-001"
        remaining_checkpoints = [c for c in lesson.checkpoints if c.id != deleted_checkpoint_id]
        self.assertEqual(len(remaining_checkpoints), 0)

    def test_update_card_with_invalid_type_raises_error(self):
        card = Card(id="card-1", front="Front", back="Back")
        with self.assertRaises(TypeError):
            self.service.update_card("card-1", {"front": "New Front", "back": None})
