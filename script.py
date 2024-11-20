import re

def fetch_email_domain(mail_id):
    domain_pattern = re.compile(r'^[^@]+@(.+)$')
    match = domain_pattern.match(mail_id)
    if match:
        return match.group(1)
    else:
        return None