EDITABLE_FIELDS = {"name", "position", "department"}

def adjust_employee_details(person: dict, alterations: dict, has_admin_rights: bool):
    if has_admin_rights:
        person.update(alterations)
    else:
        for key, value in alterations.items():
            person[key] = value
    return person