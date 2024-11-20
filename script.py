import hashlib

def encode_password(hash_algorithm: str, plain_text_pwd: bytes) -> str:
    if hash_algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algorithm} is not available")
    hasher = hashlib.new(hash_algorithm, plain_text_pwd)
    return hasher.hexdigest()