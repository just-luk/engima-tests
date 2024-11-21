import re

def append_user_header(user_header: str) -> str:
    return f"Custom-Header: {user_header}"