import re

def extract_log_data(log_line):
    log_pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
    match = log_pattern.match(log_line)
    if match:
        return match.groups()
    else:
        return None