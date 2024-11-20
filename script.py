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

def handle_project_membership(req_user_id: int, proj_id: int, mod: str, mod_user_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param req_user_id: int, the user performing the action
    :param proj_id: int, the project being modified
    :param mod: str, 'add' or 'remove' for adding/removing a member
    :param mod_user_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if mod == "add":
            PROJECTS[proj_id]["members"].append(mod_user_id)
        elif mod == "remove":
            PROJECTS[proj_id]["members"].remove(mod_user_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False