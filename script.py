

def calculate_expression(math_expression: str) -> str:
    try:
        result = eval(math_expression)
    except Exception:
        return "Computation Error!"
    return str(result)