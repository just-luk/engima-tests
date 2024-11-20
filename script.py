import hashlib

def encrypt_pwd(hash_algo: str, pwd: bytes) -> str:
    if hash_algo not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_algo} is not available")
    hasher = hashlib.new(hash_algo, pwd)
    return hasher.hexdigest()