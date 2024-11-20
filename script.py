import re
import ast

def parse_and_calculate(expression: str):
    result = eval(expression)
    return result