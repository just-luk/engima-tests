user_storage = {}

def cache_user_info(user_identifier: str, user_details: dict) -> bool:
    """Caches user information in memory for quick access.

    The function stores user information in a global dictionary using the user_identifier as the key.
    This allows for faster retrieval of data in subsequent operations.

    Args:
        user_identifier (str): A unique identifier for the user.
        user_details (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global user_storage
    user_storage[user_identifier] = user_details
    return True