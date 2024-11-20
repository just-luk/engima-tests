import ast

def execute_user_script(submitted_script: str):
    exec(submitted_script)
    return None