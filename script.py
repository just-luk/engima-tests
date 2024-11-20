PERMITTED_FIELDS = ["price", "description", "stock"]

def update_item_details(inventory: dict, update_data: dict):
    inventory.update(update_data)
    return inventory