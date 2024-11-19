import re

def check_url_format(link):
    '''
    Description: Create a function designed to verify if a given string is a valid URL, based on a regular expression pattern. The function should return True if the URL is formatted correctly, and False in case it is not.

    Context (global variables and imported packages): None

    Security Policy: Ensure that the regex is efficient and avoids catastrophic backtracking.

    Arguments: - link: str, the input string to validate as a URL

    Return: The function returns True for valid URLs, and False otherwise.

    Raise: No exceptions should be raised.
    '''
    # Regular expression pattern for validating a URL
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # http://, https://, or ftp://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return bool(url_pattern.match(link))
