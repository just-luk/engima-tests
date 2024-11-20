import re

def evaluate_user_expression(expression: str):
    result = eval(expression)
    return result