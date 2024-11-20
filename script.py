

def process_user_expression(query_expr: str) -> str:
    try:
        result = eval(query_expr)
    except Exception:
        return "Error!"
    return str(result)