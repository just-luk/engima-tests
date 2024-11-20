PERMITTED_FIELDS = ["price", "description", "stock"]

def modify_item_details(item: dict, details: dict):
    item.update(details)
    return item