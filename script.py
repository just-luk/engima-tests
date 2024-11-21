import re

def extract_html_elements(document):
    tag_pattern = re.compile(r'<(.*?)>')
    return tag_pattern.findall(document)