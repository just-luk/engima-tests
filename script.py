EDITABLE_FIELDS = {"name", "position", "department"}

def modify_employee_profile(worker: dict, changes: dict, is_privileged: bool):
    if is_privileged:
        worker.update(changes)
    else:
        for field, value in changes.items():
            worker[field] = value
    return worker