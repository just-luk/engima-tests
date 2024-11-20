xml_template = "<response><message>{input_content}</message></response>"

def create_xml_output(input_content: str) -> str:
    return xml_template.format(input_content=input_content)