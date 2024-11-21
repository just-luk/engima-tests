import hashlib

def generate_hash(algo_hash: str, pwd_input: bytes) -> bytes:
    if algo_hash not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_hash} is not available")
    hasher = hashlib.new(algo_hash, pwd_input)
    return hasher.digest()