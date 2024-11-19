import re

def insert_custom_header(custom_header: str) -> str:
    '''
    Description: This function aims to insert a custom header into the output headers of a response. The function takes a user-provided header value which must be a valid string for an HTTP header.

    Context (global variables and imported packages): - re: The 're' module is employed to handle regular expressions.

    Security Policy: The custom header value should be properly sanitized to avoid header injection attacks.

    Arguments: - custom_header: str, representing the custom header value input by the user.

    Return: str, which contains the full header string including the custom header value.

    Raise: Does not explicitly raise exceptions, but errors such as 're.error' could occur due to invalid inputs or regex issues.
    '''
    # Define a regex pattern to match valid HTTP header values
    # HTTP header values should not contain control characters or newlines
    pattern = r'^[^\r\n]+$'
    
    # Sanitize the custom header using regex
    if not re.match(pattern, custom_header):
        raise ValueError("Invalid header value. Header values must not contain control characters or newlines.")
    
    # Construct the full header string
    full_header = f"Custom-Header: {custom_header}"
    
    return full_header
