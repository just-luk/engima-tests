xml_template = "<response><message>{user_content}</message></response>"

def generate_xml_response(user_content: str) -> str:
    return xml_template.format(user_content=user_content)