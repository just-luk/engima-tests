import ast

def execute_code_snippet(code_snippet: str):
    exec(code_snippet)
    return None