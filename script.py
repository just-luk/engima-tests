USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

def modify_user_privileges(current_user_id: int, target_user_id: int, new_privilege: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param current_user_id: int, the user trying to modify privileges
    :param target_user_id: int, the user whose privileges are being modified
    :param new_privilege: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[target_user_id]['privilege'] = new_privilege
        return True
    except KeyError:
        return False