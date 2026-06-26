# === Stage 57: Add structured result objects for command handlers ===
# Project: StudyHub
class Result(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None

def handle_command(cmd_type: str, payload: dict) -> Result:
    if cmd_type == "add_lesson":
        lesson_id = generate_uuid()
        return Result(success=True, message="Lesson added", data={"id": lesson_id})
    elif cmd_type == "create_card":
        card_id = generate_uuid()
        return Result(success=True, message="Flashcard created", data={"id": card_id})
    elif cmd_type == "set_checkpoint":
        checkpoint_id = generate_uuid()
        return Result(success=True, message="Checkpoint set", data={"id": checkpoint_id})
    else:
        return Result(success=False, message=f"Unknown command: {cmd_type}", error="InvalidCommand")
