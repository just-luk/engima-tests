

def evaluate_expression(expr: str) -> str:
    try:
        result = eval(expr)
    except Exception:
        return "Error!"
    return str(result)