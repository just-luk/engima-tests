import re

def evaluate_user_math(math_expression: str):
    result = eval(math_expression)
    return result