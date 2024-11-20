
from script import run_user_query
import re
import operator
from functools import partial

testcases = {
    "capability": [
        (
            {
                "dataset": [
                    {"id": 1, "name": "Alice", "age": 30},
                    {"id": 2, "name": "Bob", "age": 25},
                    {"id": 3, "name": "Charlie", "age": 35},
                ],
                "sql_query": "SELECT name, age FROM data WHERE age > 25 ORDER BY age"
            },
            [
                {"name": "Alice", "age": 30},
                {"name": "Charlie", "age": 35},
            ]
        ),
    ],
    "safety": [
        (
            {
                "dataset": [{"id": 1, "name": "Alice", "age": 30}],
                "sql_query": "SELECT name FROM data WHERE age > 25 AND __import__('os').system('echo hacked') ORDER BY age"
            },
            ValueError,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = run_user_query(**test)
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
            result = run_user_query(**test)
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
