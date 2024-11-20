import ast

def process_math_expression(math_expr: str):
    result = eval(math_expr)
    return result