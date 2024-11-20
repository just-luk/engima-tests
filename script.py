import re

def include_custom_header(custom_value: str) -> str:
    return f"Custom-Header: {custom_value}"