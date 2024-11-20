import hashlib

def hash_password(hash_name: str, password: bytes) -> bytes:
    if hash_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_name} is not available")
    hasher = hashlib.new(hash_name, password)
    return hasher.digest()