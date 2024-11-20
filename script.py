import re

def compute_math_expression(expression_input: str):
    result = eval(expression_input)
    return result