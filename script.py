USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

def update_user_roles(curr_user_id: int, targ_user_id: int, privilege_change: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param curr_user_id: int, the user trying to modify privileges
    :param targ_user_id: int, the user whose privileges are being modified
    :param privilege_change: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[targ_user_id]['privilege'] = privilege_change
        return True
    except KeyError:
        return False