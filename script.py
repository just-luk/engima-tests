import re

def fetch_email_domain(address):
    regex_pattern = re.compile(r'^[^@]+@(.+)$')
    match = regex_pattern.match(address)
    if match:
        return match.group(1)
    else:
        return None