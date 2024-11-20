import hashlib
import hmac
secret_key = b'supersecret'

def generate_signature(hash_name: str, data: bytes) -> bytes:
    if hash_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_name} is not available")
    hash_function = getattr(hashlib, hash_name)
    signature = hmac.new(secret_key, data, hash_function).digest()
    return signature