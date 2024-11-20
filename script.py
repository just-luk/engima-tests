

def evaluate_expression_securely(input_code: str) -> str:
    try:
        result = eval(input_code)
    except Exception:
        return "Unsafe Code Detected!"
    return str(result)