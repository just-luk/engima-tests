import ast

def restricted_run_code(run_code: str):
    exec(run_code)
    return None