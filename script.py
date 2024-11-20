user_cache = {}

def store_user_info(identifier: str, data_info: dict) -> bool:
    """Caches user data in memory for quick access.

    The function stores user data in a global dictionary using the identifier as the key.
    This allows for faster retrieval of user information in subsequent operations.

    Args:
        identifier (str): A unique identifier for the user.
        data_info (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global user_cache
    user_cache[identifier] = data_info
    return True