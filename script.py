xml_template = "<response><message>{user_input}</message></response>"

def create_xml_output(user_input: str) -> str:
    return xml_template.format(user_input=user_input)