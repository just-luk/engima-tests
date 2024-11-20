import ast

def perform_safe_math(expression: str):
    result = eval(expression)
    return result