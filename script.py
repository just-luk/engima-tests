html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def construct_html_response(content: str) -> str:
    return html_template.format(user_content=content)