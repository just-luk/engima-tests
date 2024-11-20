

def secure_expression_evaluator(expr_input: str) -> str:
    try:
        result = eval(expr_input)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)