import re

def insert_header_with_sanitization(custom_header_value: str) -> str:
    return f"Custom-Header: {custom_header_value}"