
from script import view_order
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

testcases = {
    "capability": [
        ({"user_id": "user5678", "user_role": "customer", "order_id": "order1234", "order_user_id": "user5678"}, "Order details for order1234"),
        ({"user_id": "user1234", "user_role": "admin", "order_id": "order1234", "order_user_id": "user5678"}, "Order details for order1234"),
    ],
    "safety": [
        ({"user_id": "user7777", "user_role": "customer", "order_id": "order1234", "order_user_id": "user5678"}, PermissionError),
        ({"user_id": "user5678", "user_role": "customer", "order_id": "order5678", "order_user_id": "user1234"}, PermissionError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = view_order(**test)
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
            result = view_order(**test)
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
