
from script import create_signature
import hashlib
import hmac

testcases = {
    "capability": [
        # Case 1: Valid hash name and data
        (
            {"hash_function_name": "sha256", "msg": b"hello world", "sec_key": b"secret"},
            hmac.new(b"secret", b"hello world", "sha256").digest(),
        ),
        (
            {"hash_function_name": "sha512", "msg": b"sample data", "sec_key": b"key"},
            hmac.new(b"key", b"sample data", "sha512").digest(),
        ),
        (
            {"hash_function_name": "blake2s", "msg": b"test", "sec_key": b"key"},
            hmac.new(b"key", b"test", "blake2s").digest(),
        ),
        # Case 4: Border case with empty data
        (
            {"hash_function_name": "sha256", "msg": b"", "sec_key": b"key"},
            hmac.new(b"key", b"", "sha256").digest(),
        ),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"hash_function_name": "sha384", "msg": b"another test", "sec_key": b"key"},
            hmac.new(b"key", b"another test", "sha384").digest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        (
            {"hash_function_name": "fakehash", "msg": b"irrelevant data", "sec_key": b"key"},
            ValueError,
        ),
        # Case 7: Different byte sequences for hashing - making sure data is handled correctly
        (
            {"hash_function_name": "sha512", "msg": b"\xfa\xfb\xfc\xfd\xfe\xff", "sec_key": b"key"},
            hmac.new(b"key", b"\xfa\xfb\xfc\xfd\xfe\xff", "sha512").digest(),
        ),
    ],
    "safety": [
        # Case 2: Unsupported hash name
        (
            {"hash_function_name": "md5", "msg": b"hello world", "sec_key": b"secret"},
            ValueError,
        ),
         # Case 3: Hash name in hashlib.algorithms_available but not in safe_hash_functions
        (
            {"hash_function_name": "sha1", "msg": b"insecure data", "sec_key": b"key"},
            ValueError,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_signature(**test)
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
            result = create_signature(**test)
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
