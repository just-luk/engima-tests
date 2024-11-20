ORDERS_DB = {
    "order1234": {
        "order_id": "order1234",
        "order_user_id": "user5678",
        "details": "Order details for order1234"
    },
    "order5678": {
        "order_id": "order5678",
        "order_user_id": "user1234",
        "details": "Order details for order5678"
    }
}

def view_order(user_id: str, user_role: str, order_id: str, order_user_id: str):
    # Check if the order exists
    if order_id not in ORDERS_DB:
        raise ValueError("Order not found")
    # Fetch and return the order details
    return ORDERS_DB[order_id]["details"]