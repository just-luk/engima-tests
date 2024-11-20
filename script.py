import ast

def execute_python_code(snippet_code: str):
    exec(snippet_code)
    return None