

def evaluate_user_code(code_string: str) -> str:
    try:
        result = eval(code_string)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)