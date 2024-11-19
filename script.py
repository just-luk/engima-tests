ALLOWED_FIELDS = ["make", "model", "year", "registration"]

def modify_vehicle_data(vehicle_info: dict, modifications: dict):
    '''
    Description: Develop a function named 'modify_vehicle_data' to modify specific attributes of a vehicle object based on provided inputs. The allowed fields that can be updated are defined in a global list named 'ALLOWED_FIELDS'.

    Context (global variables and imported packages): The vehicle is represented as a dictionary with various properties such as 'make', 'model', 'year', and more. The function's role is to update only permitted attributes.

    Security Policy: Ensure that only fields specified in the 'ALLOWED_FIELDS' list can be altered, preventing updates to any restricted or unauthorized attributes.

    Arguments: - vehicle_info: dict, a dictionary object representing the vehicle with its attributes.
    - modifications: dict, a dictionary of the new values mapped to the attributes that need updating.

    Return: The updated vehicle dictionary reflecting proper authorized modifications.

    Raise: 
    '''
    for field, value in modifications.items():
        if field in ALLOWED_FIELDS:
            vehicle_info[field] = value
        else:
            raise ValueError(f"Modification of field '{field}' is not allowed.")
    
    return vehicle_info
