

def execute_user_input(user_code: str) -> str:
    try:
        result = eval(user_code)
    except Exception:
        return "Execution Blocked!"
    return str(result)