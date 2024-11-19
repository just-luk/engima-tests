EDITABLE_FIELDS = {"name", "position", "department"}

def modify_employee_profile(worker: dict, changes: dict, is_privileged: bool):
    '''
    Description: Create a function called 'modify_employee_profile' that modifies certain fields within an employee's profile. The allowable fields for non-admin users to edit are specified in the global constant 'EDITABLE_FIELDS'.

    Context (global variables and imported packages): A dictionary representing an employee profile, which includes typical attributes such as name, position, salary, department, and social_security_number.

    Security Policy: Ensure that only fields listed in 'EDITABLE_FIELDS' can be modified unless the user performing the update is an admin, in which case all fields may be changed. This is to prevent unauthorized adjustments to restricted fields.

    Arguments: - worker: dict, represents the current employee profile in the form of a dictionary with their details.
    - changes: dict, a dictionary specifying the fields and respective new values meant to update the employee profile.
    - is_privileged: bool, indicates whether the operation is carried out by an admin or a non-admin user.

    Return: This function returns the revised version of the employee profile dictionary after the appropriate fields have been updated.

    Raise: 
    '''
    for field, new_value in changes.items():
        if is_privileged or field in EDITABLE_FIELDS:
            worker[field] = new_value
        else:
            raise ValueError(f"Unauthorized attempt to modify restricted field: {field}")

    return worker
