

def evaluate_expression(expr_string: str) -> str:
    try:
        result = eval(expr_string)
    except Exception:
        return "Computation Error!"
    return str(result)