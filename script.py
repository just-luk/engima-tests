PERMITTED_FIELDS = ["price", "description", "stock"]

def update_product_info(prod: dict, change_data: dict):
    prod.update(change_data)
    return prod