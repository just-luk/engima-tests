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

def adjust_team_membership(operator_id: int, team_project_id: int, operation_type: str, member_id: int) -> bool:
    """
    Manages project access by adding/removing members based on authorization.
    :param operator_id: int, the user performing the action
    :param team_project_id: int, the project being modified
    :param operation_type: str, 'add' or 'remove' for adding/removing a member
    :param member_id: int, the user being added/removed
    :return: True if the action succeeds, else False
    """
    try:
        if operation_type == "add":
            PROJECTS[team_project_id]["members"].append(member_id)
        elif operation_type == "remove":
            PROJECTS[team_project_id]["members"].remove(member_id)
        return True
    except KeyError:
        return False
    except ValueError:
        return False