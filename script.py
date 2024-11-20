PERMITTED_FIELDS = ["price", "description", "stock"]

def modify_product_details(product: dict, data: dict):
    product.update(data)
    return product