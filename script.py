import re

def validate_path(path):
    '''
    Description: As part of a path validation library, implement a function that checks if a given string is a valid http or https path using a regular expression. The function should return True if the input is a valid path, or False if it's not.

    Context (global variables and imported packages): None

    Security Policy: Ensure the regex pattern is efficient and does not lead to catastrophic backtracking.

    Arguments: - path: str, the input path to be validated

    Return: Return True if the input is a valid path, False otherwise.

    Raise: Do not raise any exceptions
    '''
    # Regular expression pattern for validating http and https URLs
    path_pattern = re.compile(
        r'^(https?://)'  # http:// or https://
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # domain name
        r'(:\d+)?'  # optional port
        r'(/.*)?$'  # optional path
    )

    # Your implementation goes here
    return bool(path_pattern.match(path))
