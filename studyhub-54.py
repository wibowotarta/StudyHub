# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: StudyHub
import sys, colorama
colorama.init()
def c(text: str, fg=None, bg=None):
    codes = []
    if bg: codes.append(40 + bg)
    if fg: codes.append(30 + fg)
    return "\x1b[?" + "".join(codes) + text + "\x1b[0m" if codes else text
def print_colored(msg, *args):
    colors = {
        "header": (96,), "success": (32,), "error": (31,),
        "warning": (33,), "info": (34,), "dim": (90,)
    }
    fmt = msg.format(*args) if args else msg
    for k, v in colors.items():
        if k == "header" and fmt.startswith(("===", "#")): print(c(fmt, *v)); return
        if k == "error" and "Error" in fmt or "Traceback" in fmt: print(c(fmt, *v)); return
    print(fmt)
