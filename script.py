xml_structure = "<response><message>{client_input}</message></response>"

def craft_xml_reply(client_input: str) -> str:
    return xml_structure.format(client_input=client_input)