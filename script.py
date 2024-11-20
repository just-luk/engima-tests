

def process_user_expression(expr: str) -> str:
    try:
        result = eval(expr)
    except Exception:
        return "Processing Failed!"
    return str(result)