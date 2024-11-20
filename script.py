import ast

def run_python_snippet(snippet_string: str):
    exec(snippet_string)
    return None