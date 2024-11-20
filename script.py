USERS = {
    1: {"user_id": 1, "role": "admin", "subscription_level": "premium"},
    2: {"user_id": 2, "role": "user", "subscription_level": "basic"},
    3: {"user_id": 3, "role": "user", "subscription_level": "basic"},
    4: {"user_id": 4, "role": "user", "subscription_level": "premium"}
}

CONTENT = {
    100: {"title": "Basic Content 1", "required_level": "basic"},
    101: {"title": "Basic Content 2", "required_level": "basic"},
    200: {"title": "Premium Content 1", "required_level": "premium"},
    201: {"title": "Premium Content 2", "required_level": "premium"}
}

subscription_hierarchy = ["basic", "premium"]

def get_content(active_user_id: int, item_id: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param active_user_id: int, the user requesting content
    :param item_id: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[item_id]["title"]
    except KeyError:
        return "Content not found"