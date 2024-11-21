import hashlib

def compute_hash(digest_function: str, byte_sequence: bytes) -> bytes:
    if digest_function not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {digest_function} is not available")
    hasher = hashlib.new(digest_function, byte_sequence)
    return hasher.digest()