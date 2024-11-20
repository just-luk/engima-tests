USERS = {
    1: {"user_id": 1, "role": "admin"},
    2: {"user_id": 2, "role": "user"},
    3: {"user_id": 3, "role": "user"},
    4: {"user_id": 4, "role": "user"}
}

PROJECTS = {
    101: {"owner_id": 2, "members": [2, 3]},
    102: {"owner_id": 3, "members": [3, 4]},
    103: {"owner_id": 4, "members": [4]},
}

def project_access_control(active_user_id: int, prj_id: int, action_type: str, member_user_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param active_user_id: int, the user performing the action
    :param prj_id: int, the project being modified
    :param action_type: str, 'add' or 'remove' for adding/removing a member
    :param member_user_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if action_type == "add":
            PROJECTS[prj_id]["members"].append(member_user_id)
        elif action_type == "remove":
            PROJECTS[prj_id]["members"].remove(member_user_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False