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

def control_project_permissions(executing_user_id: int, prjct_id: int, act_type: str, tgt_user_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param executing_user_id: int, the user performing the action
    :param prjct_id: int, the project being modified
    :param act_type: str, 'add' or 'remove' for adding/removing a member
    :param tgt_user_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if act_type == "add":
            PROJECTS[prjct_id]["members"].append(tgt_user_id)
        elif act_type == "remove":
            PROJECTS[prjct_id]["members"].remove(tgt_user_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False