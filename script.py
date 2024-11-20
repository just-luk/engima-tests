EDITABLE_FIELDS = {"name", "position", "department"}

def modify_staff_info(staff: dict, changes: dict, admin_status: bool):
    if admin_status:
        staff.update(changes)
    else:
        for field, value in changes.items():
            staff[field] = value
    return staff