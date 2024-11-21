user_cache = {}

def cache_profile_data(profile_id: str, profile_data: dict) -> bool:
    """Caches user data in memory for quick access.

    The function stores user data in a global dictionary using the profile_id as the key.
    This allows for faster retrieval of user information in subsequent operations.

    Args:
        profile_id (str): A unique identifier for the user.
        profile_data (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global user_cache
    user_cache[profile_id] = profile_data
    return True