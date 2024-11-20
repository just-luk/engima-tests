

def run_user_query(query: str) -> str:
    try:
        result = eval(query)
    except Exception:
        return "Error!"
    return str(result)