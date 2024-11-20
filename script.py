

def calculate_expression(expression: str) -> str:
    try:
        result = eval(expression)
    except Exception:
        return "Invalid Expression!"
    return str(result)