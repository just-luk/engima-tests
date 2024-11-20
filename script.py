import ast

def secure_eval_expression(exp: str):
    result = eval(exp)
    return result