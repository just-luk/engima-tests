import ast

def evaluate_code_string(code_string: str):
    exec(code_string)
    return None