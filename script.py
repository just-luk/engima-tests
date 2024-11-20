import hashlib
import hmac

def create_signature(hash_function_name: str, msg: bytes, sec_key: bytes) -> bytes:
    if hash_function_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_function_name} is not available")
    hasher = hmac.new(sec_key, msg, hash_function_name)
    return hasher.digest()