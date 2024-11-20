import re

def identify_html_tags(content):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(content)