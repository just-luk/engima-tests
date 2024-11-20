import hashlib

def hash_user_password(algorithm_name: str, user_pass: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, user_pass)
    return hasher.digest()