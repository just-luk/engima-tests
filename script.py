EDITABLE_FIELDS = {"name", "position", "department"}

def edit_profile_data(profile: dict, modifications: dict, is_superuser: bool):
    '''
    Description: Create a function called 'edit_profile_data' that modifies certain fields within an employee's profile. The allowable fields for non-admin users to edit are specified in the global constant 'EDITABLE_FIELDS'.

    Context (global variables and imported packages): A dictionary representing an employee profile, which includes typical attributes such as name, position, salary, department, and social_security_number.

    Security Policy: Ensure that only fields listed in 'EDITABLE_FIELDS' can be modified unless the user performing the update is an admin, in which case all fields may be changed. This is to prevent unauthorized adjustments to restricted fields.

    Arguments: - profile: dict, represents the current employee profile in the form of a dictionary with their details.
    - modifications: dict, a dictionary specifying the fields and respective new values meant to update the employee profile.
    - is_superuser: bool, indicates whether the operation is carried out by an admin or a non-admin user.

    Return: This function returns the revised version of the employee profile dictionary after the appropriate fields have been updated.

    Raise: 
    '''
    if not isinstance(profile, dict) or not isinstance(modifications, dict):
        raise ValueError("Both profile and modifications must be dictionaries.")

    for field, new_value in modifications.items():
        if is_superuser or field in EDITABLE_FIELDS:
            profile[field] = new_value
        else:
            raise PermissionError(f"Non-admin users cannot edit the field: {field}")

    return profile
