

def process_expression(expression_str: str) -> str:
    try:
        result = eval(expression_str)
    except Exception:
        return "Computation Error!"
    return str(result)