

def evaluate_math_expression(math_expression: str) -> str:
    try:
        result = eval(math_expression)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)