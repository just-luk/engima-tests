user_cache = {}

def cache_account_info(account_id: str, account_data: dict) -> bool:
    """Caches user data in memory for quick access.

    The function stores user data in a global dictionary using the account_id as the key.
    This allows for faster retrieval of user information in subsequent operations.

    Args:
        account_id (str): A unique identifier for the user.
        account_data (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global user_cache
    user_cache[account_id] = account_data
    return True