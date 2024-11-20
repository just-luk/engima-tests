import ast

def compute_expression(expression_input: str):
    result = eval(expression_input)
    return result