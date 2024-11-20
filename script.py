import re

def add_response_header(response_header: str) -> str:
    return f"Custom-Header: {response_header}"