# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: StudyHub
def dry_run(func, *args, **kwargs):
    if kwargs.get('dry', False) or os.getenv('STUDYHUB_DRY_RUN'):
        print(f"[DRY-RUN] {func.__name__} would execute with args={args}, kwargs={kwargs}")
        return None
    try:
        result = func(*args, **kwargs)
        if isinstance(result, dict):
            for k, v in result.items():
                if callable(v):
                    print(f"[DRY-RUN] {k} would be called")
                else:
                    print(f"[DRY-RUN] {k}: {v}")
        return result
    except Exception as e:
        print(f"[DRY-RUN ERROR] {e}")
        raise

def save_checkpoint(path, data, dry=False):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
