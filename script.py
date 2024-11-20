import re
import ast

def compute_expression(expr_input: str):
    result = eval(expr_input)
    return result