import re

def get_html_tags(html_input):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(html_input)