import ast

def execute_user_code(submitted_code: str):
    exec(submitted_code)
    return None