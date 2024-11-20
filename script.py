import re
import ast

def compute_expression(expr: str):
    result = eval(expr)
    return result