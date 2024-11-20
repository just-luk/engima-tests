import re

def detect_html_tags(html_str):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(html_str)