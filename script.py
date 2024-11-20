import ast

def run_code_snippet(user_code: str):
    exec(user_code)
    return None