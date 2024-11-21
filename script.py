import re

def check_url_format(link):
    url_check = re.compile(r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$')
    return bool(url_check.match(link))