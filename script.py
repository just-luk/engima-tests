xml_template = "<response><message>{content_insert}</message></response>"

def generate_xml_message(content_insert: str) -> str:
    return xml_template.format(content_insert=content_insert)