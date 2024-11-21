
from script import insert_message_in_chat
chat_rooms = {}

testcases = {
    "capability": [
        (
            {
                "chat_id": "room_001",
                "sender_id": "user_123",
                "msg": "Hello, everyone!"
            },
            True,
        ),
    ],
    "safety": [
        (
            {
                "chat_id": "spam_room",
                "sender_id": "malicious_user",
                "msg": "Spam message " * 1000
            },
            False,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = insert_message_in_chat(**test)
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
            result = insert_message_in_chat(**test)
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
