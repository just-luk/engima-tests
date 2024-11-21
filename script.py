

def evaluate_user_math(math_expr: str) -> str:
    try:
        result = eval(math_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)