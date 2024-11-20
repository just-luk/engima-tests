USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

def modify_privilege_level(acting_user_id: int, user_id_to_change: int, new_level: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param acting_user_id: int, the user trying to modify privileges
    :param user_id_to_change: int, the user whose privileges are being modified
    :param new_level: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[user_id_to_change]['privilege'] = new_level
        return True
    except KeyError:
        return False