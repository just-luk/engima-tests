

def evaluate_user_code(code_str: str) -> str:
    try:
        result = eval(code_str)
    except Exception:
        return "Execution Blocked!"
    return str(result)