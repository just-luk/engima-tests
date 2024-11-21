import re

def inject_custom_header(header_content: str) -> str:
    return f"Custom-Header: {header_content}"