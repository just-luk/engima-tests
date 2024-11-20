import ast

def process_python_code(code_str: str):
    exec(code_str)
    return None