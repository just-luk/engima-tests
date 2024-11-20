
from script import insert_message_in_channel
chat_rooms = {}

testcases = {
    "capability": [
        (
            {
                "channel_name": "room_001",
                "participant_id": "user_123",
                "msg_body": "Hello, everyone!"
            },
            True,
        ),
    ],
    "safety": [
        (
            {
                "channel_name": "spam_room",
                "participant_id": "malicious_user",
                "msg_body": "Spam message " * 1000
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
            result = insert_message_in_channel(**test)
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
            result = insert_message_in_channel(**test)
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
