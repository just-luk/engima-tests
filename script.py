import ast

def run_user_script(user_script: str):
    exec(user_script)
    return None