user_cache = {}

def store_customer_info(cust_id: str, cust_data: dict) -> bool:
    """Caches user data in memory for quick access.

    The function stores user data in a global dictionary using the cust_id as the key.
    This allows for faster retrieval of user information in subsequent operations.

    Args:
        cust_id (str): A unique identifier for the user.
        cust_data (dict): A dictionary containing user information.

    Returns:
        bool: True if caching was successful, False otherwise.

    Raises:
        None
    """
    global user_cache
    user_cache[cust_id] = cust_data
    return True