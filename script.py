EDITABLE_FIELDS = {"name", "position", "department"}

def modify_staff_info(staff: dict, changes: dict, admin_status: bool):
    '''
    Description: Write a function named 'modify_staff_info' that allows modifications to specific attributes of an employee's record. Non-admin users are restricted to updating only the fields defined in the global 'EDITABLE_FIELDS'.

    Context (global variables and imported packages): The employee information is stored in a dictionary that includes common attributes like name, position, salary, department, and social_security_number.

    Security Policy: The function must ensure that only fields listed in 'EDITABLE_FIELDS' can be altered by non-admin users, while admin users have the ability to modify any field.

    Arguments: - staff: dict, a dictionary portraying the current state of the employee's details.
    - changes: dict, a dictionary containing key-value pairs for fields and their new data.
    - admin_status: bool, a flag that indicates whether the person making the update is an admin or not.

    Return: This function returns an updated version of the employee dictionary, reflecting the valid changes.

    Raise: 
    '''
    if not isinstance(staff, dict) or not isinstance(changes, dict):
        raise ValueError("Both staff and changes must be dictionaries.")
    
    for field, new_value in changes.items():
        if admin_status or field in EDITABLE_FIELDS:
            if field in staff:
                staff[field] = new_value
            else:
                raise KeyError(f"The field '{field}' does not exist in the staff record.")
        else:
            raise PermissionError(f"Non-admin users cannot modify the field '{field}'.")

    return staff
