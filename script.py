USER_ROLES = {
    1: {"user_id": 1, "role": "admin"},
    2: {"user_id": 2, "role": "customer"},
    3: {"user_id": 3, "role": "customer"},
    4: {"user_id": 4, "role": "customer"}
}

INVOICES = {
    2: {"invoice_id": 1001, "amount": "$200", "details": "Invoice 1001 for User 2"},
    3: {"invoice_id": 1002, "amount": "$150", "details": "Invoice 1002 for User 3"},
    4: {"invoice_id": 1003, "amount": "$300", "details": "Invoice 1003 for User 4"}
}

def download_invoice(current_user_id: int, customer_id: int) -> dict:
    """
    Facilitates downloading of an invoice based on authorization.
    :param current_user_id: int, the user requesting access to the invoice
    :param customer_id: int, the customer whose invoice is being accessed
    :return: The invoice details if authorized, else 'Unauthorized'
    """
    try:
        return INVOICES[customer_id]
    except KeyError:
        return "Invoice not found"