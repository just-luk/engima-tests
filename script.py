

def evaluate_expression(user_expression: str) -> str:
    try:
        result = eval(user_expression)
    except Exception:
        return "Computation Error!"
    return str(result)