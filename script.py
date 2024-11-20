import hashlib

def encrypt_password(algo_name: str, key: bytes) -> str:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, key)
    return hasher.hexdigest()