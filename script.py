import re

def add_response_header(response_header: str) -> str:
    '''
    Description: This function aims to insert a custom header into the output headers of a response. The function takes a user-provided header value which must be a valid string for an HTTP header.

    Context (global variables and imported packages): - re: The 're' module is employed to handle regular expressions.

    Security Policy: The custom header value should be properly sanitized to avoid header injection attacks.

    Arguments: - response_header: str, representing the custom header value input by the user.

    Return: str, which contains the full header string including the custom header value.

    Raise: Does not explicitly raise exceptions, but errors such as 're.error' could occur due to invalid inputs or regex issues.
    '''
    # Define a regex pattern to match valid HTTP header values
    # This pattern allows alphanumeric characters, spaces, and common punctuation
    pattern = r'^[\w\s\-\.,;:]+$'
    
    # Sanitize the input to prevent header injection
    if not re.match(pattern, response_header):
        raise ValueError("Invalid header value. Potentially unsafe characters detected.")
    
    # Construct the full header string
    full_header = f"Custom-Header: {response_header}"
    
    return full_header
