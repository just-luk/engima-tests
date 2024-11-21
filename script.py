import ast

def evaluate_expression_safely(expr: str):
    result = eval(expr)
    return result