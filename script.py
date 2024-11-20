import re

def insert_custom_header(user_header: str) -> str:
    return f"Custom-Header: {user_header}"