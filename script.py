

def process_user_input(user_query: str) -> str:
    try:
        result = eval(user_query)
    except Exception:
        return "Error!"
    return str(result)