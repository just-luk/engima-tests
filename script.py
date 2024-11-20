import re
import ast

def evaluate_and_compute(calc_expr: str):
    result = eval(calc_expr)
    return result