import re
import ast

def compute_expression(input_expr: str):
    result = eval(input_expr)
    return result