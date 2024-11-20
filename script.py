

def process_user_script(code_str: str) -> str:
    try:
        result = eval(code_str)
    except Exception:
        return "Execution Blocked!"
    return str(result)