

def evaluate_expression(user_expr: str) -> str:
    try:
        result = eval(user_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)