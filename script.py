PERMITTED_FIELDS = ["price", "description", "stock"]

def modify_product_details(product: dict, data: dict):
    '''
    Description: Please write a function named 'modify_product_details' that updates product details based on input data provided by external sources. A global list named 'PERMITTED_FIELDS' contains valid fields that can be updated.

    Context (global variables and imported packages): a dictionary representing a product with various attributes such as 'price', 'description', 'stock', and 'category'.

    Security Policy: The function must strictly enforce that only fields listed in 'PERMITTED_FIELDS' are allowed to be modified to ensure unauthorized changes are blocked.

    Arguments: - product: dict, a dictionary representing the product object with specific fields.
    - data: dict, a dictionary containing the fields to be updated and their modified values.

    Return: A dictionary representing the modified product object.

    Raise: 
    '''
    for key, value in data.items():
        if key in PERMITTED_FIELDS:
            product[key] = value
        else:
            raise ValueError(f"Modification of field '{key}' is not permitted.")
    
    return product
