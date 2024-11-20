PERMITTED_FIELDS = ["price", "description", "stock"]

def adjust_product_data(prod_info: dict, change_vals: dict):
    prod_info.update(change_vals)
    return prod_info