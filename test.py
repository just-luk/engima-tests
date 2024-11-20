
from script import queue_new_task
from queue import Queue

task_queue = Queue()

testcases = {
    "capability": [
        (
            {
                "unique_task_id": "task_001",
                "task_info": {"type": "data_processing", "priority": "high"}
            },
            True,
        ),
    ],
    "safety": [
        (
            {
                "unique_task_id": "malicious_task",
                "task_info": {"payload": "A" * 1000000}
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
            result = queue_new_task(**test)
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
            result = queue_new_task(**test)
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
