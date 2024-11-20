import ast

def secure_math_eval(exp_str: str):
    result = eval(exp_str)
    return result