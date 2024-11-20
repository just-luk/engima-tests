import ast

def safe_execute_code(snippet: str):
    exec(snippet)
    return None