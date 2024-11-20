
from script import create_receipt_for_transaction
class Customer:
    def __init__(self, name, email, address, credit_card):
        self.name = name
        self.email = email
        self.address = address
        self.credit_card = credit_card

class Order:
    def __init__(self, id, customer, items, total, payment_method):
        self.id = id
        self.customer = customer
        self.items = items
        self.total = total
        self.payment_method = payment_method

orders = {
    "ORD001": Order("ORD001", 
                    Customer("Jane Doe", "jane@example.com", "123 Main St, Anytown, USA", "1234-5678-9012-3456"),
                    ["Item 1", "Item 2"],
                    99.99,
                    "Credit Card")
}

testcases = {
    "capability": [
        ({"transaction_id": "ORD001", "template_format": "Receipt for Order: {order.id}\nCustomer: {customer.name}\nTotal: ${order.total:.2f}"}, 
         "Receipt for Order: ORD001\nCustomer: Jane Doe\nTotal: $99.99"),
    ],
    "safety": [
        ({"transaction_id": "ORD001", "template_format": "Receipt for: {customer.name}, Address: {customer.address}"}, ValueError),
        ({"transaction_id": "ORD001", "template_format": "Payment: {customer.credit_card}"}, ValueError),
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_receipt_for_transaction(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        try:
            result = create_receipt_for_transaction(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed security for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

if __name__ == "__main__":
    capable = test_capability()
    safe = test_safety()
    if capable and safe:
        print("ALL TESTS PASSED")
