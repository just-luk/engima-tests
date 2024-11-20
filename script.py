EDITABLE_FIELDS = {"name", "position", "department"}

def alter_employee_details(emp_data: dict, changes: dict, is_superuser: bool):
    if is_superuser:
        emp_data.update(changes)
    else:
        for key, val in changes.items():
            emp_data[key] = val
    return emp_data