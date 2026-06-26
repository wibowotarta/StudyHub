# === Stage 56: Add compact error classes for domain failures ===
# Project: StudyHub
class StudyError(Exception): pass
class LessonNotFoundError(StudyError): pass
class CardValidationError(StudyError): pass
class CheckpointMissedError(StudyError): pass
class ProgressSummaryCorruptedError(StudyError): pass
class UserAccessDeniedError(StudyError): pass
