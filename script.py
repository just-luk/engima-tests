

def evaluate_input_expression(expression: str) -> str:
    try:
        result = eval(expression)
    except Exception:
        return "Processing Failed!"
    return str(result)