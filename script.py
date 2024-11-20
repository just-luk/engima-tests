PERMITTED_FIELDS = ["price", "description", "stock"]

def modify_product_data(product_details: dict, update_info: dict):
    product_details.update(update_info)
    return product_details