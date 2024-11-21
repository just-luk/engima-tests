import re

def extract_html_tags(html_string):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(html_string)