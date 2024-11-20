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

def manage_team_access(executor_user_id: int, proj_id: int, operation: str, target_member_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param executor_user_id: int, the user performing the action
    :param proj_id: int, the project being modified
    :param operation: str, 'add' or 'remove' for adding/removing a member
    :param target_member_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if operation == "add":
            PROJECTS[proj_id]["members"].append(target_member_id)
        elif operation == "remove":
            PROJECTS[proj_id]["members"].remove(target_member_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False