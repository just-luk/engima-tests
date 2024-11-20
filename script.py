import re

def contains_dangerous_scheme(user_input: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', user_input, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', user_input, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)