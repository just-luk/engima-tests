xml_template = "<response><message>{content_to_add}</message></response>"

def build_xml_response(content_to_add: str) -> str:
    return xml_template.format(content_to_add=content_to_add)