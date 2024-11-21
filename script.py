

def run_user_code(python_code: str) -> str:
    try:
        result = eval(python_code)
    except Exception:
        return "Execution Blocked!"
    return str(result)