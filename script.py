

def evaluate_arith_expression(input_expr: str) -> str:
    try:
        result = eval(input_expr)
    except Exception:
        return "Computation Error!"
    return str(result)