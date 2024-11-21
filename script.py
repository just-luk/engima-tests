import hashlib
import hmac
primary_secret_key = b'supersecret'

def create_checksum(algorithm_name: str, message_data: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hash_function = getattr(hashlib, algorithm_name)
    signature = hmac.new(primary_secret_key, message_data, hash_function).digest()
    return signature