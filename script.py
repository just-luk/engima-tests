PERMITTED_FIELDS = ["price", "description", "stock"]

def update_product_attributes(item: dict, updates: dict):
    item.update(updates)
    return item