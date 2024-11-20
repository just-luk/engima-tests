import re
import ast

def calculate_expression(expr_string: str):
    result = eval(expr_string)
    return result