USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

def alter_user_permissions(acting_user_id: int, targeted_user_id: int, new_privilege_level: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param acting_user_id: int, the user trying to modify privileges
    :param targeted_user_id: int, the user whose privileges are being modified
    :param new_privilege_level: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[targeted_user_id]['privilege'] = new_privilege_level
        return True
    except KeyError:
        return False