

def run_user_script(script_input: str) -> str:
    try:
        result = eval(script_input)
    except Exception:
        return "Execution Blocked!"
    return str(result)