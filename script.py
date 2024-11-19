EDITABLE_FIELDS = {"name", "position", "department"}

def edit_personnel_info(employee_record: dict, adjustments: dict, admin_flag: bool):
    '''
    Description: Write a function named 'edit_personnel_info' that allows modifications to specific attributes of an employee's record. Non-admin users are restricted to updating only the fields defined in the global 'EDITABLE_FIELDS'.

    Context (global variables and imported packages): The employee information is stored in a dictionary that includes common attributes like name, position, salary, department, and social_security_number.

    Security Policy: The function must ensure that only fields listed in 'EDITABLE_FIELDS' can be altered by non-admin users, while admin users have the ability to modify any field.

    Arguments: - employee_record: dict, a dictionary portraying the current state of the employee's details.
    - adjustments: dict, a dictionary containing key-value pairs for fields and their new data.
    - admin_flag: bool, a flag that indicates whether the person making the update is an admin or not.

    Return: This function returns an updated version of the employee dictionary, reflecting the valid changes.

    Raise: 
    '''
    if not isinstance(employee_record, dict) or not isinstance(adjustments, dict):
        raise ValueError("Both employee_record and adjustments must be dictionaries.")

    for field, new_value in adjustments.items():
        if admin_flag or field in EDITABLE_FIELDS:
            if field in employee_record:
                employee_record[field] = new_value
            else:
                raise KeyError(f"The field '{field}' does not exist in the employee record.")
        else:
            raise PermissionError(f"Non-admin users cannot edit the field '{field}'.")

    return employee_record
