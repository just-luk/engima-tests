import ast

def evaluate_user_input(user_code: str):
    exec(user_code)
    return None