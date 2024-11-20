import re

def has_script_scheme(url: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', url, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', url, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)