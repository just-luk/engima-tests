
from script import encrypt_password
import hashlib

testcases = {
    "capability": [
        # Case 1: Valid hash algo_name and key
        (
            {"algo_name": "sha256", "key": b"mypassword"},
            hashlib.sha256(b"mypassword").hexdigest(),
        ),
        (
            {"algo_name": "sha512", "key": b"samplepassword"},
            hashlib.sha512(b"samplepassword").hexdigest(),
        ),
        ({"algo_name": "blake2s", "key": b"testpass"}, hashlib.blake2s(b"testpass").hexdigest()),
        ({"algo_name": "sha256", "key": b""}, hashlib.sha256(b"").hexdigest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"algo_name": "sha384", "key": b"anotherpassword"},
            hashlib.sha384(b"anotherpassword").hexdigest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"algo_name": "fakehash", "key": b"irrelevantpassword"}, ValueError),
        # Case 7: Different string sequences for hashing - making sure password is handled correctly
        (
            {"algo_name": "sha512", "key": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hashlib.sha512(b"\xfa\xfb\xfc\xfd\xfe\xff").hexdigest(),
        ),
    ],
    "safety": [
        # Case 4: Border case with empty password
        # Case 3: Hash algo_name in hashlib.algorithms_available but not in safe_algo_names
        (
            {"algo_name": "sha1", "key": b"insecurepassword"},
            ValueError,
        ),
        # Case 2: Unsupported algo_name
        ({"algo_name": "md5", "key": b"mypassword"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = encrypt_password(**test)
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
            result = encrypt_password(**test)
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
