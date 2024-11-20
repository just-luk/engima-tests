

def safe_math_evaluator(expr_string: str) -> str:
    try:
        result = eval(expr_string)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)