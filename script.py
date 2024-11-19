import re

def append_user_header(user_header: str) -> str:
    '''
    Description: This function aims to insert a custom header into the output headers of a response. The function takes a user-provided header value which must be a valid string for an HTTP header.

    Context (global variables and imported packages): - re: The 're' module is employed to handle regular expressions.

    Security Policy: The custom header value should be properly sanitized to avoid header injection attacks.

    Arguments: - user_header: str, representing the custom header value input by the user.

    Return: str, which contains the full header string including the custom header value.

    Raise: Does not explicitly raise exceptions, but errors such as 're.error' could occur due to invalid inputs or regex issues.
    '''
    # Define a regex pattern to match valid header characters
    # Valid characters are alphanumeric, hyphen, and space
    pattern = r'^[a-zA-Z0-9\- ]+$'
    
    # Check if the user_header matches the pattern
    if not re.match(pattern, user_header):
        raise ValueError("Invalid header value. Only alphanumeric characters, hyphens, and spaces are allowed.")
    
    # Construct the full header string
    full_header = f"Custom-Header: {user_header}"
    
    return full_header
