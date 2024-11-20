

def process_user_query(user_input: str) -> str:
    try:
        result = eval(user_input)
    except Exception:
        return "Error!"
    return str(result)