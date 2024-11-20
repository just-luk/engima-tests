EDITABLE_FIELDS = {"name", "position", "department"}

def adjust_employee_profile(emp: dict, changes: dict, has_admin_rights: bool):
    if has_admin_rights:
        emp.update(changes)
    else:
        for field, value in changes.items():
            emp[field] = value
    return emp