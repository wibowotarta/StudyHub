# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: StudyHub
import unittest
from studyhub.helpers import validate_lesson, create_checkpoint, normalize_card_text

class TestHelpers(unittest.TestCase):
    def test_validate_lesson_valid(self):
        self.assertTrue(validate_lesson("Math", "Algebra Basics"))
    
    def test_validate_lesson_empty_title(self):
        with self.assertRaises(ValueError):
            validate_lesson("", "Empty Title")
    
    def test_create_checkpoint_success(self):
        cp = create_checkpoint("Lesson 1", True)
        self.assertEqual(cp["title"], "Checkpoint: Lesson 1")
        self.assertTrue(cp["completed"])
    
    def test_normalize_card_text_spaces(self):
        text = "   Hello World!   "
        normalized = normalize_card_text(text)
        self.assertEqual(normalized, "Hello World!")

if __name__ == "__main__":
    unittest.main()
