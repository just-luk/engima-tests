import hashlib

def generate_hash(digest_name: str, payload: bytes) -> bytes:
    if digest_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {digest_name} is not available")
    hasher = hashlib.new(digest_name, payload)
    return hasher.digest()