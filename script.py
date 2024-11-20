EDITABLE_FIELDS = {"name", "position", "department"}

def modify_staff_details(employee_data: dict, changes: dict, is_superuser: bool):
    if is_superuser:
        employee_data.update(changes)
    else:
        for field, value in changes.items():
            employee_data[field] = value
    return employee_data