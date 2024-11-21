import re

def retrieve_domain_from_email(email_address):
    domain_pattern = re.compile(r'^[^@]+@(.+)$')
    match = domain_pattern.match(email_address)
    if match:
        return match.group(1)
    else:
        return None