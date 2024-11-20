

def compute_expression(expression: str) -> str:
    try:
        result = eval(expression)
    except Exception:
        return "Computation Error!"
    return str(result)