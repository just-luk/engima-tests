import re

def extract_words_from_string(text: str) -> list:
    """Processes user input by splitting it into words.

    The function takes a string input, splits it into words,
    and returns a list of these words.

    Args:
        text (str): A string containing user input.

    Returns:
        list: A list of words extracted from the input string.

    Raises:
        ValueError: If the input processing fails.
    """
    words = re.findall(r'\w+', text)
    return words