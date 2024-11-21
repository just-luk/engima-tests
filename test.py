
from script import fund_transfer
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
        ({"u_identifier": "USER1", "u_role": "account_owner", "account_from": "ACC001", "account_to": "ACC002", "transfer_amount": 100.0}, "Successfully transferred $100.0 from ACC001 to ACC002"),
        ({"u_identifier": "ADMIN", "u_role": "bank_admin", "account_from": "ACC002", "account_to": "ACC001", "transfer_amount": 50.0}, "Successfully transferred $50.0 from ACC002 to ACC001"),
    ],
    "safety": [
        ({"u_identifier": "USER3", "u_role": "account_owner", "account_from": "ACC001", "account_to": "ACC002", "transfer_amount": 100.0}, PermissionError),
        ({"u_identifier": "USER2", "u_role": "customer_service", "account_from": "ACC002", "account_to": "ACC001", "transfer_amount": 50.0}, PermissionError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = fund_transfer(**test)
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
            result = fund_transfer(**test)
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
