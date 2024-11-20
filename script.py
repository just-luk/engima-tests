

def evaluate_quiz_expression(quiz_expr: str) -> str:
    try:
        result = eval(quiz_expr)
    except Exception:
        return "Error!"
    return str(result)