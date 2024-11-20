cache_storage = {}

def store_user_data(uid: str, data: dict) -> bool:
    """Caches user data in memory for quick access.

    The function stores user data in a global dictionary using the uid as the key.
    This allows for faster retrieval of user information in subsequent operations.

    Args:
        uid (str): A unique identifier for the user.
        data (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global cache_storage
    cache_storage[uid] = data
    return True