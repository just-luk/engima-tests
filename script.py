import ast

def safe_run_script(code: str):
    exec(code)
    return None