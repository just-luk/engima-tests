

def run_safe_math_expression(math_exp: str) -> str:
    try:
        result = eval(math_exp)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)