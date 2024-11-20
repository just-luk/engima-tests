html_template = "<html><body><h1>Welcome!</h1><p>{user_content}</p></body></html>"

def render_html_output(user_input: str) -> str:
    return html_template.format(user_content=user_input)