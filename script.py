

def calculate_expression(ex_string: str) -> str:
    try:
        result = eval(ex_string)
    except Exception:
        return "Computation Error!"
    return str(result)