

def process_math_expr(math_input: str) -> str:
    try:
        result = eval(math_input)
    except Exception:
        return "Computation Error!"
    return str(result)