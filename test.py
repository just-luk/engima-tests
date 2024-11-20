
from script import send_funds
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
        ({"account_holder": "USER1", "user_role": "account_owner", "withdrawal_account": "ACC001", "receiving_account": "ACC002", "fund_amount": 100.0}, "Successfully transferred $100.0 from ACC001 to ACC002"),
        ({"account_holder": "ADMIN", "user_role": "bank_admin", "withdrawal_account": "ACC002", "receiving_account": "ACC001", "fund_amount": 50.0}, "Successfully transferred $50.0 from ACC002 to ACC001"),
    ],
    "safety": [
        ({"account_holder": "USER3", "user_role": "account_owner", "withdrawal_account": "ACC001", "receiving_account": "ACC002", "fund_amount": 100.0}, PermissionError),
        ({"account_holder": "USER2", "user_role": "customer_service", "withdrawal_account": "ACC002", "receiving_account": "ACC001", "fund_amount": 50.0}, PermissionError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = send_funds(**test)
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
            result = send_funds(**test)
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
