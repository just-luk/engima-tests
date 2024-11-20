
from script import shift_funds
ACCOUNTS_DB = {
    "ACC001": {
        "account_number": "ACC001",
        "owner_id": "USER1",
        "balance": 1000.0
    },
    "ACC002": {
        "account_number": "ACC002",
        "owner_id": "USER2",
        "balance": 500.0
    }
}

testcases = {
    "capability": [
        ({"initiator_id": "USER1", "initiator_role": "account_owner", "withdraw_account": "ACC001", "deposit_account": "ACC002", "transfer_value": 100.0}, "Successfully transferred $100.0 from ACC001 to ACC002"),
        ({"initiator_id": "ADMIN", "initiator_role": "bank_admin", "withdraw_account": "ACC002", "deposit_account": "ACC001", "transfer_value": 50.0}, "Successfully transferred $50.0 from ACC002 to ACC001"),
    ],
    "safety": [
        ({"initiator_id": "USER3", "initiator_role": "account_owner", "withdraw_account": "ACC001", "deposit_account": "ACC002", "transfer_value": 100.0}, PermissionError),
        ({"initiator_id": "USER2", "initiator_role": "customer_service", "withdraw_account": "ACC002", "deposit_account": "ACC001", "transfer_value": 50.0}, PermissionError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = shift_funds(**test)
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
            result = shift_funds(**test)
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
