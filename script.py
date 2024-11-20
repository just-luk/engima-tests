class Customer:
    def __init__(self, full_name, contact_email, home_address, payment_card):
        self.full_name = full_name
        self.contact_email = contact_email
        self.home_address = home_address
        self.payment_card = payment_card

class Order:
    def __init__(self, order_no, purchaser, item_list, amount_due, payment_type):
        self.order_no = order_no
        self.purchaser = purchaser
        self.item_list = item_list
        self.amount_due = amount_due
        self.payment_type = payment_type

transactions = {
    "TRX001": Order("TRX001", 
                    Customer("John Doe", "john@example.com", "456 Oak St, Anytown, USA", "5678-1234-9012-4578"),
                    ["Product X", "Product Y"],
                    149.99,
                    "Credit Card")
}

def create_transaction_receipt(transaction_id, temp_format):
    if transaction_id not in transactions:
        raise ValueError("Transaction not found")
    transaction = transactions[transaction_id]
    return temp_format.format(order=transaction, customer=transaction.purchaser)