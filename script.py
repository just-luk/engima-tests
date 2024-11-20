PERMITTED_FIELDS = ["price", "description", "stock"]

def amend_product_features(item: dict, payload: dict):
    item.update(payload)
    return item