

def parse_user_script(script_str: str) -> str:
    try:
        result = eval(script_str)
    except Exception:
        return "Execution Blocked!"
    return str(result)