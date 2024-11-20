import hashlib

def hash_password(algorithm_name: str, raw_password: bytes) -> str:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, raw_password)
    return hasher.hexdigest()