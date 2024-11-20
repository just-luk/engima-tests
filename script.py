import ast

def execute_python_script(python_code: str):
    exec(python_code)
    return None