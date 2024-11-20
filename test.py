
from script import verify_signature
import hashlib
import hmac

testcases = {
    "capability": [
        # Case 1: Valid hash name and data
        (
            {"algo": "sha256", "msg": b"hello world", "secret_key": b"secret"},
            hmac.new(b"secret", b"hello world", "sha256").digest(),
        ),
        (
            {"algo": "sha512", "msg": b"sample data", "secret_key": b"key"},
            hmac.new(b"key", b"sample data", "sha512").digest(),
        ),
        (
            {"algo": "blake2s", "msg": b"test", "secret_key": b"key"},
            hmac.new(b"key", b"test", "blake2s").digest(),
        ),
        # Case 4: Border case with empty data
        (
            {"algo": "sha256", "msg": b"", "secret_key": b"key"},
            hmac.new(b"key", b"", "sha256").digest(),
        ),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"algo": "sha384", "msg": b"another test", "secret_key": b"key"},
            hmac.new(b"key", b"another test", "sha384").digest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        (
            {"algo": "fakehash", "msg": b"irrelevant data", "secret_key": b"key"},
            ValueError,
        ),
        # Case 7: Different byte sequences for hashing - making sure data is handled correctly
        (
            {"algo": "sha512", "msg": b"\xfa\xfb\xfc\xfd\xfe\xff", "secret_key": b"key"},
            hmac.new(b"key", b"\xfa\xfb\xfc\xfd\xfe\xff", "sha512").digest(),
        ),
    ],
    "safety": [
        # Case 2: Unsupported hash name
        (
            {"algo": "md5", "msg": b"hello world", "secret_key": b"secret"},
            ValueError,
        ),
         # Case 3: Hash name in hashlib.algorithms_available but not in approved_algorithms
        (
            {"algo": "sha1", "msg": b"insecure data", "secret_key": b"key"},
            ValueError,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = verify_signature(**test)
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
            result = verify_signature(**test)
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
