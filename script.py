import hashlib
import hmac

def produce_signature(method_name: str, data: bytes, secret_key: bytes) -> bytes:
    if method_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {method_name} is not available")
    hasher = hmac.new(secret_key, data, method_name)
    return hasher.digest()