

def compute_expression(query_str: str) -> str:
    try:
        result = eval(query_str)
    except Exception:
        return "Error!"
    return str(result)