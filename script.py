EDITABLE_FIELDS = {"name", "position", "department"}

def edit_personnel_info(employee_record: dict, adjustments: dict, admin_flag: bool):
    if admin_flag:
        employee_record.update(adjustments)
    else:
        for field, value in adjustments.items():
            employee_record[field] = value
    return employee_record