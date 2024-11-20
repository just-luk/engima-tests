html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def generate_html_response(user_content: str) -> str:
    return html_template.format(user_content=user_content)