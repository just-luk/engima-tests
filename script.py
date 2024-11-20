

def evaluate_student_response(student_query: str) -> str:
    try:
        result = eval(student_query)
    except Exception:
        return "Error!"
    return str(result)