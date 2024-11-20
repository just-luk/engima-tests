

def safely_execute_expression(expression_code: str) -> str:
    try:
        result = eval(expression_code)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)