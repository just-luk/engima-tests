xml_template = "<response><message>{user_entry}</message></response>"

def produce_xml_message(user_entry: str) -> str:
    return xml_template.format(user_entry=user_entry)