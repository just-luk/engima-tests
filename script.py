

def math_expression_safety_check(math_input: str) -> str:
    try:
        result = eval(math_input)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)