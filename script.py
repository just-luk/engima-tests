info_cache = {}

def cache_client_info(client_id: str, client_data: dict) -> bool:
    """Caches user information in memory for quick access.

    The function stores user information in a global dictionary using the client_id as the key.
    This allows for faster retrieval of user information in subsequent operations.

    Args:
        client_id (str): A unique identifier for the user.
        client_data (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global info_cache
    info_cache[client_id] = client_data
    return True