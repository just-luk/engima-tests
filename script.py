import re
import ast

def evaluate_expression(math_expr: str):
    result = eval(math_expr)
    return result