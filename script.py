import re

def retrieve_email_domain(email_str):
    regex_pattern = re.compile(r'^[^@]+@(.+)$')
    match = regex_pattern.match(email_str)
    if match:
        return match.group(1)
    else:
        return None