import re
import ast

def evaluate_expression(expr: str):
    result = eval(expr)
    return result