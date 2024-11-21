

def securely_compute_expression(formula: str) -> str:
    try:
        result = eval(formula)
    except Exception:
        return "Processing Failed!"
    return str(result)