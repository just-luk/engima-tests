PERMITTED_FIELDS = ["price", "description", "stock"]

def update_item_information(product_info: dict, new_data: dict):
    product_info.update(new_data)
    return product_info