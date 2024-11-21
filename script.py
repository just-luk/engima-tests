

def evaluate_expression_safely(input_expr: str) -> str:
    try:
        result = eval(input_expr)
    except Exception:
        return "Processing Failed!"
    return str(result)