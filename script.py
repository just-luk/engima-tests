html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def build_html_output(client_message: str) -> str:
    return html_template.format(user_content=client_message)