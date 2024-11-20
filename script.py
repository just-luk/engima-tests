

def execute_user_input(user_input: str) -> str:
    try:
        result = eval(user_input)
    except Exception:
        return "Processing Failed!"
    return str(result)