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

def authorize_access(uid: int, cid: int) -> str:
    """
    Provides access to content based on the user's subscription level.
    :param uid: int, the user requesting content
    :param cid: int, the content the user wants to access
    :return: The content if access is allowed or 'Access Denied'
    """
    try:
        return CONTENT[cid]["title"]
    except KeyError:
        return "Content not found"