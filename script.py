

def compute_user_formula(equation: str) -> str:
    try:
        result = eval(equation)
    except Exception:
        return "Processing Failed!"
    return str(result)