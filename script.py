

def execute_user_input(expr: str) -> str:
    try:
        result = eval(expr)
    except Exception:
        return "Error!"
    return str(result)