

def exec_calculation(calc_string: str) -> str:
    try:
        result = eval(calc_string)
    except Exception:
        return "Computation Error!"
    return str(result)