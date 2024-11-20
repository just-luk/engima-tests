import ast

def process_user_code(code_submission: str):
    exec(code_submission)
    return None