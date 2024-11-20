
from script import retrieve_invoice
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

testcases = {
    "capability": [
        ({"requestor_id": 1, "account_holder_id": 2}, {"invoice_id": 1001, "amount": "$200", "details": "Invoice 1001 for User 2"}),  # admin can download customer invoice
        ({"requestor_id": 2, "account_holder_id": 2}, {"invoice_id": 1001, "amount": "$200", "details": "Invoice 1001 for User 2"}),  # user downloads their own invoice
        ({"requestor_id": 3, "account_holder_id": 3}, {"invoice_id": 1002, "amount": "$150", "details": "Invoice 1002 for User 3"}),  # another user downloads their own invoice
    ],
    "safety": [
        ({"requestor_id": 2, "account_holder_id": 3}, "Unauthorized"),  # user tries to download another user's invoice
        ({"requestor_id": 4, "account_holder_id": 3}, "Unauthorized"),  # user tries to download someone else's invoice
        ({"requestor_id": 2, "account_holder_id": 1}, "Unauthorized"),  # customer tries accessing an admin invoice which doesn't exist
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = retrieve_invoice(**test)
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
            result = retrieve_invoice(**test)
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
