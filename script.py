import ast

def process_code_input(code_input: str):
    exec(code_input)
    return None