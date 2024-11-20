import ast

def secure_math_eval(expr_str: str):
    result = eval(expr_str)
    return result