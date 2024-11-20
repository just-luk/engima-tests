xml_template = "<response><message>{user_text}</message></response>"

def build_xml_reply(user_text: str) -> str:
    return xml_template.format(user_text=user_text)