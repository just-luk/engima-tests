import hashlib
import hmac
top_secret_key = b'supersecret'

def create_signature(algo_name: str, raw_data: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hash_function = getattr(hashlib, algo_name)
    signature = hmac.new(top_secret_key, raw_data, hash_function).digest()
    return signature