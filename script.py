

def compute_expression_safely(user_expr: str) -> str:
    try:
        result = eval(user_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)