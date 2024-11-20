import ast

def safe_execute_operation(operation: str):
    result = eval(operation)
    return result