EDITABLE_FIELDS = {"name", "position", "department"}

def modify_employee_data(worker: dict, alterations: dict, admin_privileges: bool):
    if admin_privileges:
        worker.update(alterations)
    else:
        for field, value in alterations.items():
            worker[field] = value
    return worker