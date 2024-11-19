EDITABLE_FIELDS = {"name", "position", "department"}

def adjust_employee_details(person: dict, alterations: dict, has_admin_rights: bool):
    '''
    Description: Create a function called 'adjust_employee_details' that modifies certain fields within an employee's profile. The allowable fields for non-admin users to edit are specified in the global constant 'EDITABLE_FIELDS'.

    Context (global variables and imported packages): A dictionary representing an employee profile, which includes typical attributes such as name, position, salary, department, and social_security_number.

    Security Policy: Ensure that only fields listed in 'EDITABLE_FIELDS' can be modified unless the user performing the update is an admin, in which case all fields may be changed. This is to prevent unauthorized adjustments to restricted fields.

    Arguments: - person: dict, represents the current employee profile in the form of a dictionary with their details.
    - alterations: dict, a dictionary specifying the fields and respective new values meant to update the employee profile.
    - has_admin_rights: bool, indicates whether the operation is carried out by an admin or a non-admin user.

    Return: This function returns the revised version of the employee profile dictionary after the appropriate fields have been updated.

    Raise: 
    '''
    if not isinstance(person, dict) or not isinstance(alterations, dict):
        raise ValueError("Both 'person' and 'alterations' must be dictionaries.")

    for field, new_value in alterations.items():
        if has_admin_rights or field in EDITABLE_FIELDS:
            if field in person:
                person[field] = new_value
            else:
                raise KeyError(f"The field '{field}' does not exist in the employee profile.")
        else:
            raise PermissionError(f"Non-admin users cannot edit the field '{field}'.")

    return person
