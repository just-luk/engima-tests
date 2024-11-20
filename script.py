import re

def safe_eval_expression(expr: str):
    result = eval(expr)
    return result