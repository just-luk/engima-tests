import re

def parse_html_tags(html):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(html)