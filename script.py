import re

def process_user_input(user_input: str) -> list:
    """Processes user input by splitting it into words.

    The function takes a string input, splits it into words,
    and returns a list of these words.

    Args:
        user_input (str): A string containing user input.

    Returns:
        list: A list of words extracted from the input string.

    Raises:
        ValueError: If the input processing fails.
    """
    words = re.findall(r'\w+', user_input)
    return words