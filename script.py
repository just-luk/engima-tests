

def execute_user_expression(expression_string: str) -> str:
    try:
        result = eval(expression_string)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)