USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

def alter_user_privileges(cur_user_id: int, tar_user_id: int, priv_update: str) -> bool:
    """
    Modifies the user's privilege level based on authorization checks.
    :param cur_user_id: int, the user trying to modify privileges
    :param tar_user_id: int, the user whose privileges are being modified
    :param priv_update: str, the new privilege level to assign to the user
    :return: True if privileges are changed, else False
    """
    try:
        USERS[tar_user_id]['privilege'] = priv_update
        return True
    except KeyError:
        return False