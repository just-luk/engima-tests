import ast

def execute_user_code(script_to_execute: str):
    exec(script_to_execute)
    return None