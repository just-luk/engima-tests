

def evaluate_expression_safely(expression: str) -> str:
    try:
        result = eval(expression)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)