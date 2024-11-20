import ast

def safe_run_script(script_code: str):
    exec(script_code)
    return None