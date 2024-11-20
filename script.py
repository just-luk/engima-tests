import re

def check_javascript_scheme(url_str: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', url_str, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', url_str, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)