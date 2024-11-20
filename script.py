import re

def add_safe_header(custom_value: str) -> str:
    return f"Custom-Header: {custom_value}"