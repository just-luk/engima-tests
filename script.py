xml_pattern = "<response><message>{user_text}</message></response>"

def create_xml_reply(user_text: str) -> str:
    return xml_pattern.format(user_text=user_text)