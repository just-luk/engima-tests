

def calculate_expression(expr_input: str) -> str:
    try:
        result = eval(expr_input)
    except Exception:
        return "Computation Error!"
    return str(result)