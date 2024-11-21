import hashlib

def compute_hash(algorithm: str, content: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hasher = hashlib.new(algorithm, content)
    return hasher.digest()