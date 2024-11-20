EDITABLE_FIELDS = {"name", "position", "department"}

def update_employee_record(employee: dict, updates: dict, is_admin: bool):
    if is_admin:
        employee.update(updates)
    else:
        for field, value in updates.items():
            employee[field] = value
    return employee